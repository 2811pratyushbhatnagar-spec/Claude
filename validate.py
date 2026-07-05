#!/usr/bin/env python3
"""validate.py -- minimal repository validator. One job: catch drift and governance
violations against status.json, the single source of truth. Stdlib only.
Exit 0 = clean, 1 = flags. Intended to run before every commit.

This is deliberately small. A new check earns its place only by catching a failure
mode nothing else catches -- the same closure rule the protocol uses. Resist growth."""
import json, re, sys, os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
status = json.load(open(os.path.join(ROOT, "status.json")))
docs = glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
flags = []

# 1. version drift -- any doc stating "Ledger X ... v0.N" must match status.json
# Exempt the two HISTORICAL layers (LedgerE/ evidence log, reconciliation/ frozen snapshots):
# they are append-only records of the *path* and legitimately name superseded versions;
# drift-checking applies to current-state docs only. (Added 2026-07-05 with the A v0.2 adoption.)
HISTORICAL = (os.sep + "LedgerE" + os.sep, os.sep + "reconciliation" + os.sep)
current_docs = [p for p in docs if not any(h in p for h in HISTORICAL)]
for L, info in status["ledgers"].items():
    want = info["version"]
    pat = re.compile(r"Ledger\s+%s\b.{0,60}?v?0\.(\d+)" % L, re.S)
    for p in current_docs:
        t = open(p, encoding="utf-8", errors="ignore").read()
        for m in pat.finditer(t):
            got = "0." + m.group(1)
            if got != want:
                flags.append(f"VERSION DRIFT   {os.path.relpath(p, ROOT)}: Ledger {L} says {got}, canonical {want}")

# 2. Ledger C -- no admitted entries while canonical admitted == 0
if status["ledgers"]["C"].get("admitted", 0) == 0:
    for p in docs:
        t = open(p, encoding="utf-8", errors="ignore").read()
        if re.search(r"Admitted Entries", t) and not re.search(r"Admitted Entries\s*\n+\s*\*?\(?none", t, re.I):
            flags.append(f"LEDGER C        {os.path.relpath(p, ROOT)}: lists an admitted entry; canonical admitted=0")

# 3. Ledger D -- never cited as evidence
for p in docs:
    t = open(p, encoding="utf-8", errors="ignore").read()
    for m in re.finditer(r"[^.\n]*Ledger D[^.\n]*", t):
        if re.search(r"\b(proves|is evidence|because Ledger D|establishes that)\b", m.group(0), re.I):
            flags.append(f"D-AS-EVIDENCE   {os.path.relpath(p, ROOT)}: '{m.group(0).strip()[:70]}'")

if flags:
    print(f"validate: {len(flags)} flag(s)  [{len(docs)} docs vs status.json]")
    for f in flags:
        print("  " + f)
    sys.exit(1)
print(f"validate: clean  [{len(docs)} docs vs status.json]")

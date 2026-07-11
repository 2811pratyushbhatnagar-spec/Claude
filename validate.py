#!/usr/bin/env python3
"""validate.py -- minimal repository validator. One job: catch drift and governance
violations against status.json, the single source of truth. Stdlib only.
Exit 0 = clean, 1 = flags. Runs as part of run_checks.py and before commits.

Ported 2026-07-05 from the mounted repo's design (its HISTORICAL exemption and the
Ledger-C/D guards are genuine improvements; adopted under the dual-agreement rule).
A new check earns its place only by catching a failure mode nothing else catches."""
import json, re, sys, os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
status = json.load(open(os.path.join(ROOT, "status.json"), encoding="utf-8"))
docs = [p for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
        if os.sep + ".git" + os.sep not in p]
flags = []

# 0. ROOT OF TRUST -- verify the CONSTITUTIONAL CORE first. If the core is compromised,
# nothing downstream is trustworthy; fail immediately, run nothing else.
import hashlib
mf = os.path.join(ROOT, "MANIFEST.sha256.json")
if not os.path.exists(mf):
    print("validate: 1 flag(s)")
    print("  MANIFEST ABSENT  MANIFEST.sha256.json missing -- cryptographic freeze not in force")
    sys.exit(1)
manifest = json.load(open(mf, encoding="utf-8"))
core_flags = []
for rel, want in manifest.get("core", {}).items():
    p = os.path.join(ROOT, rel)
    got = hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.exists(p) else None
    if got != want:
        core_flags.append(f"CORE COMPROMISED  {rel}: constitutional-core hash mismatch -- "
                          f"core changes are Class-A only; nothing downstream is trustworthy")
if core_flags:
    print(f"validate: {len(core_flags)} CORE flag(s) -- downstream checks NOT run")
    for f in core_flags: print("  " + f)
    sys.exit(1)

# 1. version drift -- any current-state doc stating "Ledger X ... v0.N" must match status.json.
# HISTORICAL layers are exempt: they are append-only records of the *path* and legitimately
# name superseded versions. Exempt: LedgerE/, reconciliation/, archive/, handoffs/, audits/,
# .automation/ (records), and the generated views (regenerated, not hand-drifted).
HISTORICAL = tuple(os.sep + d + os.sep for d in
                   ("LedgerE", "reconciliation", "archive", "handoffs", "audits", ".automation"))
GENERATED = ("SNAPSHOT.md", "DECISIONS.md", "EVIDENCE-RIVER.md")  # river projects HISTORICAL rows
current = [p for p in docs if not any(h in p for h in HISTORICAL)
           and os.path.basename(p) not in GENERATED]
for L, info in status["ledgers"].items():
    want = info["version"]
    pat = re.compile(r"Ledger\s+%s\b.{0,60}?v?0\.(\d+)" % L, re.S)
    for p in current:
        t = open(p, encoding="utf-8", errors="ignore").read()
        # changelog blocks inside the canonical ledger legitimately name prior versions
        t = re.sub(r"\*\*Changelog\.\*\*.*?(?=\n## )", "", t, flags=re.S)
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

# 4. cryptographic freeze -- remaining pinned content must match MANIFEST.sha256.json
# (core was already verified at step 0). "Frozen" is a system property, not a convention.
for rel, want in manifest.get("files", {}).items():
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        flags.append(f"FROZEN MISSING  {rel}: pinned in manifest but absent")
        continue
    got = hashlib.sha256(open(p, "rb").read()).hexdigest()
    if got != want:
        flags.append(f"FROZEN CHANGED  {rel}: content differs from pinned hash -- requires a "
                     f"human-authorized version bump + re-pin (Class A for Ledger A/B)")

if flags:
    print(f"validate: {len(flags)} flag(s)  [{len(docs)} docs vs status.json]")
    for f in flags: print("  " + f)
    sys.exit(1)
print(f"validate: clean  [{len(docs)} docs vs status.json; manifest-pinned content verified]")

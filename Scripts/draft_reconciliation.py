#!/usr/bin/env python3
"""draft_reconciliation.py -- scaffold a dated reconciliation snapshot DRAFT.  [tooling; NOT canon]

Writes a pre-filled template to .automation/ for you to complete and -- if you choose -- freeze
as a dated snapshot under reconciliation/. Drafting is procedures-only; ADMITTING is Tier-3,
yours alone. This script performs no governance action and never overwrites an existing draft.
"""
import os, glob, hashlib, json, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def canon_hash():
    files = [os.path.join(ROOT, "status.json")] + sorted(
        p for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
        if not os.path.relpath(p, ROOT).split(os.sep)[0].startswith(".git"))
    h = hashlib.sha256()
    for p in files:
        with open(p, "rb") as f:
            h.update(hashlib.sha256(f.read()).hexdigest().encode())
    return h.hexdigest()[:12]


def main():
    status = json.load(open(os.path.join(ROOT, "status.json"), encoding="utf-8"))
    L = status["ledgers"]
    today = datetime.date.today().isoformat()
    ledgerline = " · ".join(f"{k} {v['version']}/{v['state']}" for k, v in L.items())
    outdir = os.path.join(ROOT, ".automation")
    os.makedirs(outdir, exist_ok=True)
    outp = os.path.join(outdir, f"reconciliation-draft-{today}.md")
    if os.path.exists(outp):
        print(f"draft already exists, not overwriting: {os.path.relpath(outp, ROOT)}")
        return
    body = f"""# Reconciliation DRAFT — {today}   (canon {canon_hash()})

*Auto-scaffolded, NON-CANON. Fill the blanks, then — if you choose — freeze it as a dated
snapshot under reconciliation/ (admitting is Tier-3, yours alone). Ledger E gets the matching
append. This template performs no governance action.*

Ledger state at draft time: {ledgerline}

## What was reconciled
- Topic: Round-2 reconciliation of the two parallel Ledger-A efforts (per priorities.md)
- Which construction won: _______________________________________________
- Why (evidence on BOTH sides): _________________________________________

## What stays open
- _______________________________________________________________________

## Ledger E candidate row (draft — you admit)
- {today} — reconciliation: <one line of what happened, including any negative result>
"""
    with open(outp, "w", encoding="utf-8") as f:
        f.write(body)
    print(f"[drafted] {os.path.relpath(outp, ROOT)}")


if __name__ == "__main__":
    main()

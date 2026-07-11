#!/usr/bin/env python3
"""pin_manifest.py -- (re)generate MANIFEST.sha256.json, the cryptographic freeze.

*** HUMAN AUTHORIZATION REQUIRED ***
Running this tool is meaningful ONLY as part of a human-authorized version bump (Class A for
Ledger A/B content; Class B for governance docs) or the initial baseline pin. Automation/workers
must never run it: the manifest is in worker_guard's GOVERNED set, and validate.py fails on any
pinned-content change not accompanied by a matching manifest update. That is the point --
"frozen" is a system property, not a social convention.

Usage: python pin_manifest.py --authorize "<who/why>"   (refuses without --authorize)
"""
import argparse, hashlib, json, os, datetime, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# CONSTITUTIONAL CORE: the smallest set whose integrity every other check depends on.
# validate.py verifies these hashes FIRST (root of trust). Core changes are Class-A only.
CORE = [
    "DECISION-CLASSES.md",          # class-assignment rules
    "WORKER-CONTRACT.md",           # worker boundary + packet schema
    "SUBSTANTIAL-RESULT-CHECKLIST-DRAFT.md",
    "validate.py",                  # validator definitions
    "Scripts/worker_guard.py",      # boundary enforcement
    "Scripts/cycle_check.py",       # legacy router (escalation-path runner)
    "Scripts/stage0_gate.py",       # THE ROUTER (steward directive 2026-07-06): wake logic /
                                    # gate / event triggers -- scripts decide whether models run
    "DEPENDENCIES.json",            # dependency schema
    "GOVERNANCE-VERSION.json",      # governance version + stopping rule + core closure
]
PINNED = [
    "LedgerA/ledger_A_canonical.md",
    "LedgerA/archive/ledger_A_math_v0.1_frozen.md",
    "LedgerA/archive/ledger_A_math_v0.2_canonical.md",
    "LedgerB/protocol_ledger.md",
    "LedgerB/kernel.md",
    "reconciliation/reconciliation_2026-07-04.md",
    "protocols/README.md",
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--authorize", required=True,
                    help="who authorizes this pin and why (recorded in the manifest)")
    args = ap.parse_args()
    def sha(rel):
        p = os.path.join(ROOT, rel)
        return hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.exists(p) else None
    core = {rel: sha(rel) for rel in CORE if sha(rel)}
    files = {rel: sha(rel) for rel in PINNED if sha(rel)}
    for prf in sorted(glob.glob(os.path.join(ROOT, "protocols", "*.json"))):
        rel = os.path.relpath(prf, ROOT).replace(os.sep, "/")
        files[rel] = sha(rel)
    manifest = {
        "_meta": {
            "note": "Cryptographic freeze: validate.py verifies 'core' hashes FIRST (root of trust - if the core is compromised nothing downstream is trustworthy), then 'files'. Any byte change without a human-authorized re-pin FAILS validation (core changes are Class-A; Ledger A/B changes are Class-A). Baseline pin records existing state only - pinning is not a new freeze decision.",
            "generated_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
            "authorized_by": args.authorize,
        },
        "core": core,
        "files": files,
    }
    out = os.path.join(ROOT, "MANIFEST.sha256.json")
    json.dump(manifest, open(out, "w", encoding="utf-8"), indent=2)
    print(f"pinned {len(files)} file(s) -> MANIFEST.sha256.json")
    for rel in sorted(files): print("  " + rel)

if __name__ == "__main__":
    main()

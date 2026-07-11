# Publication-Readiness view — GENERATED, not canonical; regenerable anytime.
# Reads status.json + questions.json. Never mutates anything (governance: views only).
import json, os, sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
status = json.load(open(os.path.join(HERE, "status.json"), encoding="utf-8"))
qreg = json.load(open(os.path.join(HERE, "questions.json"), encoding="utf-8"))
qs = qreg["questions"]
L = status["ledgers"]
AREAS = {   # derived display strings (unified schema, 2026-07-05)
    "Mathematics":    {"status": f"Ledger A frozen v{L['A']['version']} canonical"},
    "Protocol":       {"status": f"Ledger B frozen v{L['B']['version']}; testing, not extension"},
    "Correspondence": {"status": f"empty by design; admitted={L['C'].get('admitted', 0)}; "
                                 f"candidate queue: {len(L['C'].get('candidate_queue', []))} (unadmitted)"},
    "Ontology":       {"status": L['D']['state']},
    "Journal":        {"status": status["journal"]["state"] + "; non-citable by ledgers"},
    "Publication":    {"status": status["publication"]["state"] + " — " + status["publication"]["note"]},
}
status = dict(status); status["areas"] = AREAS

def count(pred): return sum(1 for q in qs if pred(q))
conj = count(lambda q: q["state"] == "conjecture")
opn = count(lambda q: q["state"] in ("open", "investigating"))
pend = count(lambda q: q.get("band") == "pending material")
held = count(lambda q: "ratif" in q.get("next_action", "").lower())
human = count(lambda q: q["owner"] == "human" and q["state"] not in ("theorem", "withdrawn"))

OK, WARN = "✓", "⚠"
rows = []
math_block = f"not ready: {conj} conjecture(s) pending audit/ratification, {opn} open, {pend} pending-material"
rows.append(("Mathematics", status["areas"]["Mathematics"]["status"],
             OK if (conj == 0 and opn == 0) else WARN,
             "—" if (conj == 0 and opn == 0) else math_block))
rows.append(("Protocol", status["areas"]["Protocol"]["status"], OK,
             "frozen; reopens only on observed friction from real use"))
rows.append(("Correspondence", status["areas"]["Correspondence"]["status"], OK,
             "empty is a success state; admission is Tier-3"))
rows.append(("Ontology", status["areas"]["Ontology"]["status"], OK,
             "allowed empty; P1 held as question schema"))
rows.append(("Journal", status["areas"]["Journal"]["status"], OK,
             "external, labelled exploration; borrows no ledger authority"))
pub_block = (f"not ready: {conj} conjecture(s), {opn} open question(s), {pend} pending-material, "
             f"{human} item(s) awaiting human action; paper deferred (judgment, not procedure)")
rows.append(("Publication", status["areas"]["Publication"]["status"], WARN, pub_block))

W = (16, 52, 5, 70)
print(f"PUBLICATION READINESS — generated view (not canonical) · Class-D artifact · {qreg['_meta']['created']} registry")
print("-" * sum(W))
print(f"{'Area':<{W[0]}}{'Status':<{W[1]}}{'Rdy':<{W[2]}}Blocking / note")
print("-" * sum(W))
for a, s, r, b in rows:
    print(f"{a:<{W[0]}}{s[:W[1]-1]:<{W[1]}}{r:<{W[2]}}{b}")
print("-" * sum(W))
print(f"registry: {len(qs)} questions | states: "
      + ", ".join(f"{st}={count(lambda q, st=st: q['state']==st)}"
                  for st in qreg["_meta"]["states"] if count(lambda q, st=st: q['state']==st)))
print("governance: state flips to 'theorem', Ledger-C admissions, and publication are Tier-3 (Pratyush).")

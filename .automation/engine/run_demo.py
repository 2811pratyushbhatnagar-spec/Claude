"""Offline demo. 1 ChatGPT-path + 2 DIFFERENTIATED Claude-paths => genuinely
independent. Shows (1) the invariant stabilising and the loop stopping by
STABILITY not stage-count, and (2) the echo pathology when the two Claude paths
collapse to one.  Run:  python run_demo.py"""
from agents import MockWorker
from orchestrator import run
from invariant import extract_invariant

CORE  = ["invariant-of-a-diagram", "P-dependence-is-real", "I-may-not-exist"]
NOISE = {"gpt": ["gpt-hunch-1","gpt-hunch-2","gpt-hunch-3"],
         "ca":  ["ca-hunch-1","ca-hunch-2","ca-hunch-3"],
         "cb":  ["cb-hunch-1","cb-hunch-2","cb-hunch-3"]}

def three(independent=True):
    return [MockWorker("gpt","chatgpt","literature",CORE,NOISE["gpt"],1),
            MockWorker("claude_A","claude","first-principles",CORE,NOISE["ca"],2),
            MockWorker("claude_B","claude",
                       "counterexample" if independent else "first-principles",
                       CORE,NOISE["cb"],3)]

print("=== convergence: 1 ChatGPT + 2 differentiated Claude paths ===")
r = run("What survives across representations of O?", three(True),
        n_independent=2, tau=0.0, logdir="runs")
for h in r["history"]:
    print(f"  r{h['round']:>2} {h['model']:>7}/{h['path']:<15} {h['role']:<12}"
          f" delta={h['delta']:.2f} paths={h['independent_paths']} inv={h['invariant']}")
print(f"  -> stopped_by={r['stopped_by']}  invariant={r['invariant']}"
      f"  survived {r['independent_paths']}/{r['n_independent_required']} independent paths\n")

print("=== why the 2 Claudes must differ (drop the ChatGPT leg, N=2) ===")
same = extract_invariant(
   [MockWorker("claude_A","claude","first-principles",CORE,[],2).represent("q","C",9),
    MockWorker("claude_B","claude","first-principles",CORE,[],3).represent("q","C",9)], 2)
diff = extract_invariant(
   [MockWorker("claude_A","claude","first-principles",CORE,[],2).represent("q","C",9),
    MockWorker("claude_B","claude","counterexample",CORE,[],3).represent("q","C",9)], 2)
print(f"  same path : independent_paths={same.independent_paths}  invariant={sorted(same.claims)}"
      f"   <- echo: 2 bodies, 1 path -> nothing promotes")
print(f"  diff path : independent_paths={diff.independent_paths}  invariant={sorted(diff.claims)}"
      f"   <- 2 real paths -> the core promotes")

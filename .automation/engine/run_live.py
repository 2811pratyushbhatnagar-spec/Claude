"""Live wiring of the refined triad (run at the machine, Chrome connected).

Refined topology (steward, 2026-07-07):
  BLIND PAIR (independence unit, CROSS-MODEL) -- built in parallel, blind to each other:
     claude_builder : model=claude,  evidence_path=first-principles
     gpt_builder    : model=chatgpt, evidence_path=literature  (reached via Chrome)
  INTEGRATOR NODE (a second Claude, NOT a blind builder) = THIS orchestrating process:
     - Consensus Synthesizer (extract the invariant)
     - orientation holder    (set the next mandate via the scheduler)
     - chat manager          (drive the logged-in ChatGPT tab, run the handoff)

The two builders answer BLIND; the integrator acts only on the summaries. The
orchestrator writes <mailbox>/requests/<agent>-r<n>.json and waits for
<mailbox>/responses/<agent>-r<n>.json. The integrator Claude fulfils:
  - claude_builder-* via a Claude subagent on the assigned mandate;
  - gpt_builder-*    by driving ChatGPT in Chrome and writing the reply's claims back.
Each response file is JSON: {"claims": ["some-claim", "not other-claim"]}."""
from orchestrator import run_convergence
from agents import MailboxWorker

MAILBOX = "runs/live"

def builders():
    return [MailboxWorker("claude_builder", "claude",  "first-principles", MAILBOX),
            MailboxWorker("gpt_builder",     "chatgpt", "literature",       MAILBOX)]

if __name__ == "__main__":
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else open("QUESTION.txt").read().strip()
    print(run_convergence(q, builders(), n_independent=2, tau=0.0, logdir="runs/live/log"))

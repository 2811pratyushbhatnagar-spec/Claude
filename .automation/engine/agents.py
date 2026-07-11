"""Worker adapters. The deterministic core only calls .represent(); HOW a worker
produces a representation is the pluggable part.

- MockWorker      : seeded, offline -> the loop is testable with no live model.
- MailboxWorker   : live adapter via a filesystem handoff. The MEDIATOR Claude
                    (the one holding Chrome) fulfils the ChatGPT request by
                    driving the logged-in ChatGPT tab and writing the reply back;
                    Claude requests are fulfilled by Claude subagents. See README."""
from __future__ import annotations
import json, random, time
from pathlib import Path
from invariant import Representation

class MockWorker:
    def __init__(self, agent_id, model, evidence_path, core, noise_pool, seed=0):
        self.agent_id, self.model, self.evidence_path = agent_id, model, evidence_path
        self.core = list(core); self.noise_pool = list(noise_pool)
        self.rng = random.Random(seed)
    def represent(self, question, role, rnd):
        # idiosyncratic noise shrinks as rounds progress -> the invariant settles
        k = max(0, len(self.noise_pool) - rnd)
        noise = self.rng.sample(self.noise_pool, min(k, len(self.noise_pool)))
        claims = set(self.core) | set(noise)
        return Representation(self.agent_id, self.model, self.evidence_path,
                              role, frozenset(claims))

class MailboxWorker:
    """Live adapter: write a request file, wait for a response file. Fulfilled
    out-of-band by the mediator (ChatGPT via Chrome) or a Claude subagent."""
    def __init__(self, agent_id, model, evidence_path, mailbox, timeout=1800):
        self.agent_id, self.model, self.evidence_path = agent_id, model, evidence_path
        self.mailbox, self.timeout = Path(mailbox), timeout
    def represent(self, question, role, rnd):
        req = self.mailbox / "requests"; res = self.mailbox / "responses"
        req.mkdir(parents=True, exist_ok=True); res.mkdir(parents=True, exist_ok=True)
        tag = f"{self.agent_id}-r{rnd}"
        (req / f"{tag}.json").write_text(json.dumps(
            {"agent": self.agent_id, "model": self.model,
             "evidence_path": self.evidence_path, "role": role,
             "round": rnd, "question": question}, indent=2))
        target = res / f"{tag}.json"; waited = 0
        while not target.exists() and waited < self.timeout:
            time.sleep(2); waited += 2
        if not target.exists():
            raise TimeoutError(f"no response for {tag} within {self.timeout}s")
        data = json.loads(target.read_text())
        return Representation(self.agent_id, self.model, self.evidence_path,
                              role, frozenset(data["claims"]))

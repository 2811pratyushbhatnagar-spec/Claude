#!/usr/bin/env python3
"""
status_page.py -- generate status.html (kanban board) for the reversible-contact framework.

Derived VIEW only: reads status.json (source of truth) + priorities.md (your editable board),
runs validate.py, reads the latest Ledger E snapshot. Renders; never edits canon, never makes a
governance decision. Each kanban card links to a fresh Claude chat prefilled with that item.

Usage: python status_page.py [--repo PATH] [--out PATH]
"""
import argparse, glob, hashlib, html, json, os, re, subprocess, sys, datetime, urllib.parse

def esc(x): return html.escape(str(x))

def inline_md(s):
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    return s

def split_card(item):
    m = re.match(r"\*\*(.+?)\*\*(.*)$", item)
    if m:
        title = esc(m.group(1).strip())
        body = re.sub(r"^[\s—:\-]+", "", m.group(2).strip())
        return title, inline_md(body)
    return "", inline_md(item)

CLAUDE_NEW = "https://claude.ai/new?q="

def card_link(lane_title, item_text):
    plain = re.sub(r"[*`]", "", item_text).strip()
    prompt = ("I'm working on my reversible-contact research framework. On my priority board "
              "this item is in the \"%s\" lane:\n\n%s\n\n"
              "Explain and summarise what it involves and why it matters, then guide me step by "
              "step on what's needed to move it forward. Governance rule: promoting a conjecture "
              "to a theorem, admitting a Ledger C entry, changing Ledger B, adding ontology (D), "
              "or publishing are my decisions alone — help me prepare them, don't make them."
              ) % (lane_title, plain)
    return CLAUDE_NEW + urllib.parse.quote(prompt)

def canon_hash(repo):
    h = hashlib.sha256()
    files = [os.path.join(repo, "status.json")] if os.path.exists(os.path.join(repo, "status.json")) else []
    for p in glob.glob(os.path.join(repo, "**", "*.md"), recursive=True):
        if os.path.relpath(p, repo).split(os.sep)[0].startswith((".git", "site")):
            continue
        files.append(p)
    for p in sorted(set(files)):
        rel = os.path.relpath(p, repo).replace(os.sep, "/")
        with open(p, "rb") as f:
            h.update(rel.encode()); h.update(hashlib.sha256(f.read()).hexdigest().encode())
    return h.hexdigest()

def run_validate(repo):
    vp = os.path.join(repo, "validate.py")
    if not os.path.exists(vp):
        return None, "validate.py not found"
    try:
        r = subprocess.run([sys.executable, vp], cwd=repo, capture_output=True, text=True, timeout=120)
        return r.returncode, ((r.stdout or "") + (r.stderr or "")).strip()
    except Exception as e:
        return None, "validate error: %s" % e

def git_head(repo):
    try:
        r = subprocess.run(["git", "-C", repo, "rev-parse", "--short", "HEAD"],
                           capture_output=True, text=True, timeout=15)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    except Exception:
        pass
    return None

def read_priorities(repo):
    p = os.path.join(repo, "priorities.md")
    if not os.path.exists(p):
        return None, []
    updated, sections, cur = None, [], None
    for raw in open(p, encoding="utf-8", errors="ignore"):
        s = raw.strip(); low = s.lower()
        if low.startswith("*updated") or low.startswith("updated:"):
            updated = s.strip("* ").split(":", 1)[-1].strip(); continue
        if s.startswith("## "):
            cur = (s[3:].strip(), []); sections.append(cur); continue
        if cur is not None and (s.startswith("- ") or s.startswith("* ")):
            cur[1].append(s[2:].strip())
    return updated, sections

def latest_E_block(repo):
    p = os.path.join(repo, "LedgerE", "ledger_E_evidence_log.md")
    if not os.path.exists(p):
        return None, []
    lines = open(p, encoding="utf-8", errors="ignore").read().splitlines()
    idx = [i for i, l in enumerate(lines) if l.strip().startswith("## ")]
    if not idx:
        return None, []
    start = idx[-1]; title = lines[start].strip()[3:].strip(); rows = []
    for l in lines[start + 1:]:
        s = l.strip()
        if s.startswith("## "):
            break
        if s.startswith("|") and s.endswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            rows.append(cells)
    return title, rows

def lane_class(title):
    t = title.lower()
    if "attention" in t or "blocker" in t or "block" in t: return "attn"
    if "progress" in t or "doing" in t: return "prog"
    if "next" in t or "queue" in t or "backlog" in t or "todo" in t or "to do" in t: return "next"
    if "done" in t or "recent" in t or "shipped" in t: return "done"
    return "next"

CSS = """
:root{color-scheme:light;--bg:#faf9f7;--card:#fff;--ink:#1a1a1a;--muted:#6b6b6b;--line:#e6e3de;--accent:#b8563f;--ok:#2f7d4f;--flag:#c0392b;--chip:#f0ede8}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;padding:20px}
.wrap{max-width:1100px;margin:0 auto}h1{font-size:21px;margin:0 0 2px}.sub{color:var(--muted);font-size:13px;margin-bottom:14px}
.badge{display:inline-block;padding:2px 10px;border-radius:20px;font-size:12px;font-weight:600;color:#fff}
.b-ok{background:var(--ok)}.b-flag{background:var(--flag)}
.bh{display:flex;align-items:baseline;gap:10px;margin:8px 0 8px}
.bh .t{font-size:13px;font-weight:700;letter-spacing:.02em}.bh .upd{color:var(--muted);font-size:12px}
.hint{font-size:12px;color:var(--muted);margin:0 0 10px}
.kanban{display:flex;gap:12px;overflow-x:auto;padding:2px 2px 12px;-webkit-overflow-scrolling:touch}
.lane{flex:0 0 260px;min-width:260px;background:#f4f1ec;border:1px solid var(--line);border-radius:12px;display:flex;flex-direction:column}
.lane-h{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;padding:10px 12px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--line)}
.lane-h .cnt{background:#fff;border:1px solid var(--line);border-radius:20px;padding:0 8px;font-size:11px;color:var(--muted);font-weight:600}
.cards{padding:10px;display:flex;flex-direction:column;gap:8px;min-height:8px}
.card{background:#fff;border:1px solid var(--line);border-left:4px solid #cbd5e1;border-radius:8px;padding:9px 11px;box-shadow:0 1px 2px rgba(0,0,0,.05)}
.card .c-t{font-size:13px;font-weight:650;margin-bottom:2px}.card .c-b{font-size:12.5px;color:#555;line-height:1.45}
.card code{background:var(--chip);padding:1px 5px;border-radius:4px;font-size:11.5px}
a.card{display:block;text-decoration:none;color:inherit;cursor:pointer;transition:background .12s,box-shadow .12s}
a.card:hover{background:#fcfbfa;box-shadow:0 2px 8px rgba(0,0,0,.10)}
a.card .go{display:inline-block;margin-top:6px;font-size:11px;color:var(--muted)}
a.card:hover .go{color:#1d4ed8}
.lane.attn{background:#fff7ed}.lane.attn .lane-h{color:#b45309}.lane.attn .card{border-left-color:#d97706}
.lane.prog .lane-h{color:#1d4ed8}.lane.prog .card{border-left-color:#3b82f6}
.lane.next .lane-h{color:#475569}.lane.next .card{border-left-color:#94a3b8}
.lane.done .lane-h{color:var(--ok)}.lane.done .card{border-left-color:#4ea172}.lane.done .card .c-b{color:var(--muted)}
.meta{display:flex;flex-wrap:wrap;gap:8px 16px;font-size:12px;color:var(--muted);margin:14px 0 20px}
.meta code{background:var(--chip);padding:1px 6px;border-radius:4px;color:#333}
h2{font-size:14px;margin:24px 0 8px;padding-bottom:5px;border-bottom:1px solid var(--line)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}
.lc{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 14px}
.lc h3{margin:0 0 4px;font-size:14px;display:flex;justify-content:space-between;gap:8px}.lc .v{font-size:11px;color:var(--muted)}
.state{font-size:11px;text-transform:uppercase;letter-spacing:.04em;color:var(--accent);font-weight:600}
.q{font-size:12.5px;color:#444;margin:5px 0 0}.ok{font-size:11.5px;color:var(--muted);margin-top:5px}
.open{margin:6px 0 0;padding-left:15px;font-size:12px;color:#555}
.gov{background:#fff8f2;border:1px solid #f0dccb;border-radius:10px;padding:12px 14px;font-size:12.5px}.gov ul{margin:6px 0 0;padding-left:18px}
table{border-collapse:collapse;width:100%;font-size:12px;background:#fff;border:1px solid var(--line);border-radius:8px;overflow:hidden}
th,td{text-align:left;padding:7px 9px;border-bottom:1px solid var(--line);vertical-align:top}th{background:var(--chip);font-size:10.5px;text-transform:uppercase;color:#555}
tr:last-child td{border-bottom:0}.foot{color:var(--muted);font-size:12px;margin-top:22px;border-top:1px solid var(--line);padding-top:12px}
@media(max-width:600px){body{padding:12px}.lane{flex-basis:82vw;min-width:82vw}.grid{grid-template-columns:1fr}}
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo"); ap.add_argument("--out")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo) if a.repo else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    status = json.load(open(os.path.join(repo, "status.json")))
    vcode, vout = run_validate(repo); clean = (vcode == 0)
    chash = canon_hash(repo); gh = git_head(repo)
    now = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    p_updated, p_sections = read_priorities(repo)
    e_title, e_rows = latest_E_block(repo)
    names = {"A": "Mathematics", "B": "Protocol", "C": "Correspondence", "D": "Ontology", "E": "Evidence Log"}

    p = []
    p.append("<!doctype html><html lang=en><head><meta charset=utf-8>")
    p.append("<meta name=viewport content='width=device-width,initial-scale=1'>")
    p.append("<title>reversible-contact — board</title><style>" + CSS + "</style></head><body><div class=wrap>")
    p.append("<h1>reversible-contact &mdash; board</h1>")
    p.append("<div class=sub>Derived read-only view of <code>priorities.md</code> + <code>status.json</code>. Not canon, not a governance act.</div>")

    # --- Layer-1 "Mission Control" attention strip (Class-D view; three lines, nothing more) ---
    try:
        qreg = json.load(open(os.path.join(repo, "questions.json"), encoding="utf-8"))["questions"]
        live_A = [q for q in qreg if q.get("decision_class") == "A"
                  and q["state"] in ("open", "conjecture", "investigating")]
        live_A.sort(key=lambda q: (q["id"] != "Q-GOV-V2-FREEZE",))  # freeze ratification first
        nxt = live_A[0] if live_A else None
        openq = next((q for q in qreg if q["owner"] == "auto" and q["state"] == "open"), None)
        bf_line = ""
        bfp = os.path.join(repo, ".automation", "bf_state.json")
        if os.path.exists(bfp):
            bf1 = json.load(open(bfp, encoding="utf-8"))["queue"][0]
            bf_line = " · BF-1 n=4: %.1f%%" % (100.0 * bf1["next_F"] / bf1["space"])
        p.append("<div class=bh><span class=t>Mission control</span></div><div class=hint>")
        p.append("MACHINE: %s · canon <code>%s</code>%s<br>" % (
            ("<strong style='color:#2e7d32'>GREEN</strong> (validate clean)" if clean
             else "<strong style='color:#c62828'>RED</strong> (validate flagged)"),
            esc((gh or chash)[:12]), esc(bf_line)))
        if nxt:
            p.append("NEXT HUMAN DECISION (Class A): <strong>%s</strong> — %s<br>" %
                     (esc(nxt["id"]), esc(nxt["next_action"][:140])))
        if openq:
            p.append("CURRENT OPEN QUESTION: <strong>%s</strong> — %s" %
                     (esc(openq["id"]), esc(openq["statement"][:140])))
        p.append("</div>")
    except Exception as e:
        p.append("<div class=hint>mission-control strip unavailable: %s</div>" % esc(e))

    if p_sections:
        p.append("<div class=bh><span class=t>Priority board</span>")
        if p_updated: p.append("<span class=upd>updated " + esc(p_updated) + "</span>")
        p.append("</div><div class=hint>Tap any card to open a Claude chat about that item.</div><div class=kanban>")
        for title, items in p_sections:
            p.append("<div class='lane %s'><div class=lane-h><span>%s</span><span class=cnt>%d</span></div><div class=cards>" %
                     (lane_class(title), esc(title), len(items)))
            for it in items:
                t, b = split_card(it)
                p.append("<a class=card target=_blank rel=noopener href=\"%s\">" % card_link(title, it))
                if t: p.append("<div class=c-t>%s</div>" % t)
                if b: p.append("<div class=c-b>%s</div>" % b)
                p.append("<span class=go>Open in Claude &rarr;</span></a>")
            p.append("</div></div>")
        p.append("</div>")

    badge = "<span class='badge b-ok'>validate: clean</span>" if clean else "<span class='badge b-flag'>validate: FLAGGED</span>"
    p.append("<div class=meta>" + badge)
    p.append("<span>canon updated: <code>%s</code></span>" % esc(status.get("updated", "?")))
    p.append("<span>generated: <code>%s</code></span>" % esc(now))
    p.append("<span>fingerprint: <code>%s</code></span>" % esc(gh or ("canon:" + chash[:10])))
    p.append("</div>")

    p.append("<h2>Ledgers</h2><div class=grid>")
    for k in ("A", "B", "C", "D", "E"):
        i = status["ledgers"].get(k, {})
        p.append("<div class=lc><h3><span>Ledger %s &middot; %s</span><span class=v>v%s</span></h3>" %
                 (k, esc(names.get(k, i.get("name", ""))), esc(i.get("version", "?"))))
        p.append("<div class=state>%s</div>" % esc(i.get("state", "")))
        if i.get("question"): p.append("<div class=q>%s</div>" % esc(i["question"]))
        if i.get("admitted") is not None: p.append("<div class=ok>Admitted entries: %s</div>" % esc(i["admitted"]))
        if i.get("open"):
            p.append("<ul class=open>")
            for o in i["open"]:
                p.append("<li>%s</li>" % esc(o))
            p.append("</ul>")
        p.append("</div>")
    p.append("</div>")

    gov = status.get("governance", {}).get("tier3_human_only", [])
    if gov:
        p.append("<h2>Governance &mdash; Tier-3 (human only)</h2><div class=gov>These are Pratyush's alone; automation and this view never perform them.<ul>")
        for g in gov: p.append("<li>%s</li>" % esc(g))
        p.append("</ul></div>")

    if e_title:
        p.append("<h2>Ledger E &mdash; latest snapshot (%s)</h2>" % esc(e_title))
        if e_rows:
            head = e_rows[0]; body = e_rows[1:]
            p.append("<table><tr>")
            for c in head: p.append("<th>%s</th>" % esc(c))
            p.append("</tr>")
            for r in body:
                p.append("<tr>")
                for c in r: p.append("<td>%s</td>" % esc(c))
                p.append("</tr>")
            p.append("</table>")

    p.append("<div class=foot>Stewarded by Pratyush. Edit <code>priorities.md</code> and rerun <code>python Scripts/status_page.py</code> to update. Derived view; the ledgers and <code>status.json</code> remain the source of truth.</div>")
    p.append("</div></body></html>")
    doc = "".join(p)

    out = a.out or os.path.join(repo, "status.html")
    try:
        with open(out, "w", encoding="utf-8") as f: f.write(doc)
        print("wrote " + out)
    except Exception:
        alt = out + "." + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".html"
        with open(alt, "w", encoding="utf-8") as f: f.write(doc)
        print("wrote " + alt)

if __name__ == "__main__":
    main()

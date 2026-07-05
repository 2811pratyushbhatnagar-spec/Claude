#!/usr/bin/env python3
"""
status_page.py -- generate a static status.html for the reversible-contact framework.

A derived VIEW only: reads status.json (the single source of truth), runs validate.py,
and reads the latest Ledger E snapshot. It renders, it never edits canon and never makes
a governance decision. Regenerate any time; it is not committed as canon.

Usage: python status_page.py [--repo PATH] [--out PATH]
Default out = <repo>/status.html (falls back to a timestamped name if it cannot overwrite).
"""
import argparse, glob, hashlib, html, json, os, subprocess, sys, datetime

def canon_hash(repo):
    h = hashlib.sha256()
    files = [os.path.join(repo, "status.json")] if os.path.exists(os.path.join(repo, "status.json")) else []
    for p in glob.glob(os.path.join(repo, "**", "*.md"), recursive=True):
        if os.path.relpath(p, repo).split(os.sep)[0].startswith(".git"):
            continue
        files.append(p)
    for p in sorted(set(files)):
        rel = os.path.relpath(p, repo).replace(os.sep, "/")
        with open(p, "rb") as f:
            fh = hashlib.sha256(f.read()).hexdigest()
        h.update(rel.encode()); h.update(fh.encode())
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

def latest_E_block(repo):
    p = os.path.join(repo, "LedgerE", "ledger_E_evidence_log.md")
    if not os.path.exists(p):
        return None, []
    lines = open(p, encoding="utf-8", errors="ignore").read().splitlines()
    idx = [i for i, l in enumerate(lines) if l.strip().startswith("## ")]
    if not idx:
        return None, []
    start = idx[-1]
    title = lines[start].strip()[3:].strip()
    rows = []
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

CSS = """
:root{--bg:#faf9f7;--card:#fff;--ink:#1a1a1a;--muted:#6b6b6b;--line:#e6e3de;--accent:#b8563f;--ok:#2f7d4f;--flag:#c0392b;--chip:#f0ede8}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;padding:32px}
.wrap{max-width:920px;margin:0 auto}h1{font-size:22px;margin:0 0 2px}.sub{color:var(--muted);font-size:13px;margin-bottom:18px}
.badge{display:inline-block;padding:2px 10px;border-radius:20px;font-size:12px;font-weight:600;color:#fff}
.b-ok{background:var(--ok)}.b-flag{background:var(--flag)}
.meta{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:12.5px;color:var(--muted);margin:10px 0 22px}
.meta code{background:var(--chip);padding:1px 6px;border-radius:4px;color:#333}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin-bottom:22px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.card h3{margin:0 0 6px;font-size:15px;display:flex;justify-content:space-between;align-items:baseline;gap:8px}
.card .v{font-size:11.5px;color:var(--muted);font-weight:500}
.state{font-size:11px;text-transform:uppercase;letter-spacing:.04em;color:var(--accent);font-weight:600}
.q{font-size:13px;color:#444;margin:6px 0 0}.ok{font-size:12px;color:var(--muted);margin-top:6px}
.open{margin:8px 0 0;padding-left:16px;font-size:12.5px;color:#555}.open li{margin:1px 0}
h2{font-size:15px;margin:26px 0 8px;padding-bottom:5px;border-bottom:1px solid var(--line)}
.gov{background:#fff8f2;border:1px solid #f0dccb;border-radius:10px;padding:12px 16px;font-size:13px}
.gov ul{margin:6px 0 0;padding-left:18px}.gov li{margin:2px 0}
table{border-collapse:collapse;width:100%;font-size:12.5px;background:#fff;border:1px solid var(--line);border-radius:8px;overflow:hidden}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--chip);font-size:11px;text-transform:uppercase;letter-spacing:.03em;color:#555}
tr:last-child td{border-bottom:0}
.foot{color:var(--muted);font-size:12px;margin-top:24px;border-top:1px solid var(--line);padding-top:12px}
"""

def esc(x): return html.escape(str(x))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo"); ap.add_argument("--out")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo) if a.repo else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    status = json.load(open(os.path.join(repo, "status.json")))
    vcode, vout = run_validate(repo)
    clean = (vcode == 0)
    chash = canon_hash(repo)
    gh = git_head(repo)
    now = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    e_title, e_rows = latest_E_block(repo)

    names = {"A": "Mathematics", "B": "Protocol", "C": "Correspondence", "D": "Ontology", "E": "Evidence Log"}
    p = []
    p.append("<!doctype html><html lang=en><head><meta charset=utf-8>")
    p.append("<meta name=viewport content='width=device-width,initial-scale=1'>")
    p.append("<title>reversible-contact — status</title><style>" + CSS + "</style></head><body><div class=wrap>")
    p.append("<h1>reversible-contact &mdash; framework status</h1>")
    p.append("<div class=sub>Canonical view generated from <code>status.json</code>. A derived read-only view &mdash; not canon, not a governance act.</div>")
    badge = "<span class='badge b-ok'>validate: clean</span>" if clean else "<span class='badge b-flag'>validate: FLAGGED</span>"
    p.append("<div>" + badge + "</div>")
    p.append("<div class=meta>")
    p.append("<span>updated (canon): <code>%s</code></span>" % esc(status.get("updated", "?")))
    p.append("<span>generated: <code>%s</code></span>" % esc(now))
    p.append("<span>canon: <code>%s</code></span>" % esc(chash[:12]))
    p.append("<span>git: <code>%s</code></span>" % esc(gh or "none (content-hash)"))
    p.append("<span>validate: <code>%s</code></span>" % esc((vout or "").splitlines()[0] if vout else "n/a"))
    p.append("</div>")

    p.append("<h2>Ledgers</h2><div class=grid>")
    for k in ("A", "B", "C", "D", "E"):
        i = status["ledgers"].get(k, {})
        p.append("<div class=card><h3><span>Ledger %s &middot; %s</span><span class=v>v%s</span></h3>" %
                 (k, esc(names.get(k, i.get("name", ""))), esc(i.get("version", "?"))))
        p.append("<div class=state>%s</div>" % esc(i.get("state", "")))
        if i.get("question"): p.append("<div class=q>%s</div>" % esc(i["question"]))
        if i.get("success"): p.append("<div class=ok>Success: %s</div>" % esc(i["success"]))
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
        p.append("<h2>Governance &mdash; Tier-3 (human only)</h2>")
        p.append("<div class=gov>These moves are Pratyush's alone. Automation and this view never perform them.<ul>")
        for g in gov:
            p.append("<li>%s</li>" % esc(g))
        p.append("</ul></div>")

    arch = status.get("architecture", {})
    if arch:
        p.append("<h2>Architecture</h2><div class=gov style='background:#f7f9f8;border-color:#dfe8e4'>")
        p.append("Shape: <code>%s</code> &middot; state: <code>%s</code><br>Invariant: <b>%s</b></div>" %
                 (esc(" / ".join(arch.get("shape", []))), esc(arch.get("state", "")), esc(arch.get("invariant", ""))))

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

    p.append("<div class=foot>Stewarded by Pratyush. &nbsp;This page is a derived view; the ledgers and <code>status.json</code> remain the source of truth. Regenerate with <code>python Scripts/status_page.py</code>.</div>")
    p.append("</div></body></html>")
    doc = "".join(p)

    out = a.out or os.path.join(repo, "status.html")
    try:
        with open(out, "w", encoding="utf-8") as f:
            f.write(doc)
        print("wrote " + out)
    except Exception:
        alt = out + "." + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".html"
        with open(alt, "w", encoding="utf-8") as f:
            f.write(doc)
        print("wrote " + alt + " (could not overwrite " + out + ")")

if __name__ == "__main__":
    main()

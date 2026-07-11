# Put the status board on your phone (Cloudflare Pages, private)

You publish one file — `status.html` (the derived board), never the ledgers — to a
Cloudflare Pages URL, then lock it to your email with Cloudflare Access. The Stage-0 gate task
(`reversible-contact-stage0-gate`, Windows Task Scheduler, every 5 hours, deterministic - no model)
refreshes `status.html`; you re-run the deploy to push the latest to your phone.

## One-time setup (~10 min)

1. **Install Node.js** (LTS) from https://nodejs.org — this gives you `npx`. Skip if you
   already have it. (Nothing else to install; Wrangler runs via `npx`.)

2. **Sign in to Cloudflare.** Open PowerShell in this folder
   (Shift + right-click the folder → *Open PowerShell window here*) and run:
   ```
   npx --yes wrangler login
   ```
   Approve in the browser — this links Wrangler to *your* Cloudflare account.

3. **Create the Pages project** (once):
   ```
   npx --yes wrangler pages project create reversible-contact-status --production-branch main
   ```

4. **Deploy.** Double-click **`deploy_status.bat`**. When it finishes it prints a URL like
   `https://reversible-contact-status.pages.dev` — that's your link.

## Make it private (do this right after the first deploy)

Until you do this, the URL is reachable by anyone who has it. Lock it down:

5. Cloudflare dashboard → **Zero Trust** → **Access** → **Applications** → *Add an
   application* → **Self-hosted**.
6. Application domain: your `reversible-contact-status.pages.dev` URL. Name it anything.
7. Add a policy: **Action = Allow**, **Include → Emails →** your email
   (`2811pratyushbhatnagar@gmail.com`). Save.
8. Now opening the URL (on your phone or anywhere) asks for a one-time code emailed to you.
   Only you get in.

## Refreshing the phone view later

- The Stage-0 gate task rewrites `status.html` every 5 hours (pure script, zero model tokens);
  the old 5-hourly Dispatch cycle is retired. Editing `priorities.md` and
  rerunning `python Scripts/status_page.py` also refreshes it.
- To push the latest to your phone URL, double-click **`deploy_status.bat`** again.

*The deployed page is a read-only snapshot of status.json + priorities.md. It is not canon
and performs no governance action.*

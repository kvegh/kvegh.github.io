# Karoly “Charlie” Vegh — Ansible automation projects

A personal project showcase for Karoly “Charlie” Vegh, Ansible Solution Architect,
focused on practical Red Hat Ansible Automation Platform use cases. The projects
lead the page; a small adjacent introduction supplies the author name and role.

**Website:** https://kvegh.github.io/
**Archive:** https://kvegh.github.io/archive/
**Current homepage version:** 0.0.4

The catalogue follows the public
[AAP Advanced Features umbrella](https://github.com/kvegh/AAP-advanced-features).
It lists its 14 projects with short descriptions, repository links and available
visualizations. Plans are described as plans: in particular, scanning and
extracting configuration from running AAP instances is an AutoDeploy aim.
The Windows visualization uses the approved
[AAP edition](https://kvegh.github.io/disconnected-windows-patching/demo-with-aap/).
Screenshots and embedded diagrams are distinguished from interactive walkthroughs.

## Structure and publishing

- `index.html`: complete homepage content; works without JavaScript.
- `assets/site.css`: responsive layout and presentation; no external font service.
- `VERSION`: authoritative numeric homepage version, also present in page metadata.
- `archive/index.html`: the previous homepage content with its original notes link.
- `archive/README.md`: byte-identical original homepage source from `14ecf44`.
- `tree/pages/SILUAIDWTLUA/README.md`: original notes, retained at their original URL.
- `tests/test_site.py`: repeatable HTTP functional verification.
- `design_decisions_history.md`: approved choices, history and implementation references.

The existing GitHub Pages setup publishes the root of `main` with HTTPS. Plain
HTML and CSS require no package manager, build framework, backend, secrets or
installed dependencies. Keep the existing GitHub Pages Markdown rendering enabled:
adding `.nojekyll` would risk breaking the original notes page. No new GitHub
Actions workflow is included. GitHub's existing Pages service still performs its
normal publication when `main` changes.

For a local homepage/archive preview, use Python 3's standard HTTP server:

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000/` and `http://localhost:8000/archive/`. This simple
server does not render the original Markdown notes; their public URL is verified
against the actual Pages deployment instead.

## Functional verification

Prerequisites: Python 3 with its standard library, outbound HTTPS access to the
public deployed site, and a checkout matching the version being verified. No
protected input, login, browser or dependency installation is required. Run from
the repository root after Pages finishes publishing:

```sh
python3 -B tests/test_site.py --base-url https://kvegh.github.io/
```

The test fetches the real homepage, linked stylesheet, archive and original notes
URL. It checks version metadata, the author and role, all 14 distinct project
repository links, the selected Windows visualization, section navigation, original
homepage content and the preserved notes/reference URL. It prints `PASS` lines
and exits zero on success; any failed assertion or HTTP/TLS error exits nonzero.
The test is read-only and safe to repeat. It does not exercise project demos,
access AAP or change any remote resource. Checks of external project destinations
and manual visualization discovery are separate from this deployed-page test.

Browser layout, screenshots, keyboard interaction and desktop/mobile rendering
were not tested: the owner chose to proceed without downloading a missing browser.
Responsive CSS and semantic HTML are present; they do not establish observed
browser behavior. A formal automation code review or AAP functional acceptance is
not claimed for this static website.

## Manual visualization maintenance

The owner explicitly rejected scheduled GitHub Actions checks. Perform discovery
**only when the owner instructs it**; do not add schedules or issue notifications.

1. Read the current umbrella project list and each relevant public project's
   documentation and public visualization source. Do not infer a published page
   solely from a conventional `github.io` address or the presence of HTML files.
2. Verify the documented public destination and distinguish interactive
   walkthroughs, screenshots, diagrams and actual application dashboards.
3. Update the relevant homepage link and concise description only from evidence.
   Retain the approved Windows AAP-edition link unless the owner changes it.
4. Advance `VERSION`, matching homepage metadata and the stylesheet version query, update this README and the
   decision history, and run the deployed-site test after normal publication.

## Preservation and recovery

The earlier Git history remains intact. The former homepage content is available
under `/archive/`, and the notes remain at `/tree/pages/SILUAIDWTLUA/`. Original
source preservation is anchored to commit `14ecf44`. Use an ordinary reviewed Git
revert to roll back a future site change; do not rewrite historical commits.


## Verified publication

Version 0.0.3 was published from functional source
[`a282be7`](https://github.com/kvegh/kvegh.github.io/commit/a282be7083ac82316d45e1d1182bbb0f7e05edea).
GitHub Pages built that exact revision on 2026-11-14 at 05:54:22 UTC. The
version-controlled HTTP functional test passed all three groups against the
actual public site at 05:54:59 UTC: homepage/catalogue/styles, archived homepage,
and original notes URL/content. Browser rendering remains unverified as agreed.

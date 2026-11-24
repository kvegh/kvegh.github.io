# Karoly “Charlie” Vegh — Projects and code

A personal project showcase for Karoly “Charlie” Vegh, Ansible Solution Architect,
covering advanced Ansible Automation Platform use cases alongside other code
projects. The projects lead the page; a small adjacent introduction supplies the
author name and role.

**Website:** https://kvegh.github.io/
**Archive:** https://kvegh.github.io/archive/
**Current homepage version:** 0.2.3

The catalogue has two sections, with jump links at the top:

- **Advanced AAP usecases**: 13 AAP and supporting automation projects drawn from
  the public [AAP Advanced Features umbrella](https://github.com/kvegh/AAP-advanced-features).
- **Random code musings**: the owner-selected Vortex Panic, Command Center NG and
  Assistant Team projects. Hetzner redeploy is not a separate showcase project
  yet and is intentionally omitted.

All 16 entries link to their repositories. AutoDeploy, AIOps and Windows use
the three supplied screenshot thumbnails and supported first-step visualization
links. RHEL Sniperpatching also links directly to its interactive walkthrough.
CCNG has laptop/mobile previews that open the full-size screenshots.
Vortex Panic has a matching thumbnail that opens the full-size supplied screenshot,
alongside its existing playable GitHub Pages simulation link. Its entry includes
the owner-provided VORTEX PANIC expansion and a Hitchhiker’s Guide reference. No
Assistant Team visualization was identified; its repository link is provided.

Plans remain labelled as plans, including AutoDeploy's scan-and-extract aim.
The Windows visualization retains the approved AAP-edition URL.

## Structure and publishing

- `index.html`: complete homepage content; works without JavaScript.
- `assets/site.css`: responsive layout and presentation; no external font service.
- `assets/thumbnails/`: the supplied PNG screenshots and existing public CCNG
  laptop/mobile images, preserved unchanged.
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
URL. It checks version metadata, the author and role, all 16 distinct project
repository links and their two-section placement, the selected Windows
visualization, the RHEL Sniperpatching walkthrough in its own project entry,
section navigation, original homepage content and the preserved notes/reference URL. It also verifies all six
thumbnail destinations, descriptions and served PNG/JPEG bytes against their
originals in this checkout. It prints `PASS` lines
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

1. Read the current umbrella list and the explicitly selected other projects'
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

Version 0.2.0 was published from functional source
[4917fb5](https://github.com/kvegh/kvegh.github.io/commit/4917fb591b3aa64c280a6216be2469877abef79b).
GitHub Pages built that exact revision on 2026-11-14 at 08:01:42 UTC. The
version-controlled HTTP test passed all four groups against the public site:
16 projects in the two approved sections, both jump links and styles; five
original screenshot files, descriptions and intended destinations; archived
homepage; and original notes URL/content. First-step behavior was checked
against visualization source. Browser rendering and interaction remain unverified.

Version 0.2.1 adds the Vortex Panic screenshot from functional source
[fd1ac98](https://github.com/kvegh/kvegh.github.io/commit/fd1ac9814833f15d3a8c50b84c3b7cc0fa9375b1).
GitHub Pages built it on 2026-11-14 at 17:04:17 UTC. The same deployed HTTP
check passed all four groups, including all six original images and their
intended destinations. Browser rendering remains unverified.

Version 0.2.3 adds the RHEL Sniperpatching visualization link from functional
source [262685c](https://github.com/kvegh/kvegh.github.io/commit/262685c409b8c94cbe83d6e97731345cfdfd4eba).
GitHub Pages published that revision on 2026-11-24 at 09:11:07 CET; the deployed
HTTP check passed all four groups, including the new link in its project entry.
The newly supplied sniperpatching screenshot is pending access to its original
file. Browser rendering remains unverified.

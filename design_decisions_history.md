# Design decisions and implementation history

## 2026-11-14 — Personal AAP project homepage and preservation

Date: 2026-11-14 UTC. Exact user-decision timestamps were not captured in this
file. Authority: the owner requested the project list first, reviewed it, then
instructed creation at the main `kvegh.github.io` address with the old page
archived at `/archive/`.

- Use the existing personal Pages repository and its existing `main`-root
  publishing setup. The owner chose this main address instead of a project
  subpath under the umbrella repository.
- The owner explicitly approved HTML. Use plain HTML and CSS with complete
  source content, no framework, JavaScript dependency or backend. This keeps
  publication and ongoing editing simple. A Markdown-based page was offered
  as the alternative and was not selected.
- Preserve the former homepage source exactly under `archive/README.md`, serve
  its content at `/archive/`, and retain the original notes source and URL.
  Keep the existing Markdown renderer; do not add `.nojekyll`.
- Include all 14 public umbrella projects with the supplied author name and
  role and short descriptions. State that AutoDeploy *aims* to scan and extract
  running AAP configuration. Use only the approved Windows AAP-edition
  visualization link. Do not imply planned functionality is already complete.
- Visualization discovery is manual and only follows an owner instruction.
  The owner explicitly rejected the proposed weekly GitHub Actions check and
  repository-issue notifications. Do not configure them.
- Use version `0.0.1` for the first versioned homepage implementation. Earlier
  repository content had no version metadata; its history is retained.
- Verify the actual deployed site with a small Python standard-library HTTP
  check covering homepage, catalogue, styles, archive and original notes. This
  supporting code is needed for repeatable functional verification; no test
  framework or installed third-party dependency is required.
- The existing Playwright package had no browser executable. The owner chose
  to proceed without browser checks rather than download Chromium. Do not
  install it; report visual rendering as unverified.

Initial implementation: `616cf95e707f4e60b117d20d110aa7ce047ce703` (0.0.1),
published over SSH. Pages built the exact revision at 05:48:51 UTC after a
45.027-second build. Homepage and archive HTTP assertions passed.

### Deployed-test correction — 2026-11-14

The initial HTTP test assumed the original notes reference URL would render as
an HTML link. Bounded inspection beginning at 05:49:33 UTC confirmed the existing
renderer preserves it as plain text. The original notes source is byte-identical
to `14ecf44`; do not change that historical content to satisfy the test.

Correct the test to require the preserved reference URL as text or a link.
Version 0.0.2 records this supporting-code patch, with matching page metadata and
documentation. The first failed-test timestamp and active/waiting split were not
captured. Full deployed re-verification is pending at this entry. The correction
commit is `65bda9742b202efb5815dac7a780d3927397f97c`.

## Historical source reconstruction — 2020

These are observations from Git history, not reconstructed owner approvals or
undocumented architectural rationale. Commit author timestamps use `+01:00`.

- `c76ab02` — initial homepage README, 2020-11-27 13:04:31 +01:00.
- `e717f33` — notes source added under `tree/pages/SILUAIDWTLUA/`,
  2020-11-27 13:12:29 +01:00. Intermediate notes revisions remain in history.
- `14ecf44` — homepage added its public notes link,
  2020-11-28 16:05:15 +01:00. This is the pre-redesign preservation baseline.

The original rationale and any approvals for these historical changes are
unknown. Their implementation is evidenced by the named commits.


### Direct process-diagram link — 2026-11-14

The approved catalogue identified an embedded Mermaid review-process diagram.
Add a separate, accurately labelled Process diagram link to that public README
section, alongside the repository link. It is not described as an interactive
walkthrough. Version 0.0.3 records this presentation correction; no schedule,
script or dependency was added. Implementation: `a282be7083ac82316d45e1d1182bbb0f7e05edea`. Pages built
that exact source at 05:54:22 UTC (36.441 seconds).


## 2026-11-14 — Published functional verification

At 05:54:59 UTC, `python3 -B tests/test_site.py --base-url
https://kvegh.github.io/` exited zero against the actual public site, version
0.0.3, functional revision `a282be7083ac82316d45e1d1182bbb0f7e05edea`.
All three result groups passed: homepage author/version/14 distinct repositories/
selected Windows link/navigation/styles; archived homepage content and notes
destination; original rendered notes and preserved reference URL. The test's
recorded execution duration was 0.721 seconds. Source preservation also confirmed
exact archived README and unchanged original notes relative to `14ecf44`.

The test-expectation correction is
`65bda9742b202efb5815dac7a780d3927397f97c`; its Pages build completed at
05:52:02 UTC (30.399 seconds). Initial homepage implementation remains
`616cf95e707f4e60b117d20d110aa7ce047ce703`. This final entry records evidence;
it does not change the tested HTML, CSS or test.

The exact first failed-test time was not captured. The known investigation
window from 05:49:33 UTC to successful verification was 5 minutes 26 seconds.
Active effort versus native-approval and publication waiting was not separately
measured. The original issue was a test assumption about legacy Markdown
rendering, resolved without changing the historical notes.

No scheduled discovery, GitHub Actions workflow, notification issue, new service
or dependency was added. Browser visual checks remain unperformed by explicit
owner choice. HTTP acceptance does not establish observed desktop/mobile layout
or functionality of the linked AAP projects.


## 2026-11-14 — Put projects first and reduce author prominence

The owner found the personal heading too large and asked for modest presentation:
focus on the projects, with a humble author introduction beside them. Use a
compact project-led heading and a small adjacent name/role block. Remove the
oversized personal hero, decorative platform figure and repeated bottom biography;
reduce introductory spacing so the project list starts sooner. Keep all 14
project descriptions, repository/visualization links and archive behavior.

This is the owner's requested presentation correction within the approved static
HTML/CSS design, version 0.0.4. No framework, schedule or browser installation
is introduced. Browser rendering remains unverified under the existing owner
choice. Implementation: `3d25f3275a837967f036cbef6132b9383413354f`.
The stylesheet URL includes the matching version query so previously cached
CSS does not hide the layout change. Independent source review confirmed the
14 project entries and their links remained byte-identical, with archive and
original notes untouched.

SSH publication succeeded, and Pages built the exact revision on 2026-11-14
from 06:04:26 to 06:05:03 UTC (37.243 seconds). At 06:05:30 UTC the existing
HTTP functional test passed all three result groups against the public site,
version 0.0.4, in 0.725 seconds. This records HTTP/source verification; visual
browser behavior remains unobserved under the owner's existing choice.


## 2026-11-14 — Supplied visualization thumbnails

The owner supplied three screenshots and asked for clickable thumbnails on the
respective AutoDeploy, AIOps and Windows project entries. Preserve the original
PNG bytes, contain each whole image in a small responsive preview (maximum
320px wide), include descriptive alternative text and lazy-load the images.
This is a minor feature, version 0.1.0, using existing HTML/CSS and static assets.

The screenshots depict later stages, but each link must open the beginning.
Current public initialization code confirms supported first-step destinations:
AutoDeploy `#separation`, AIOps `#step=1`, and the bare Windows AAP-edition URL
which initializes stage zero. No unsupported query parameter was introduced.
The owner also requested the same screenshots in those three public READMEs.

Extend the existing deployed HTTP check to verify the three image destinations,
alt text and exact PNG bytes in addition to the existing catalogue/archive tests.
No framework, browser installation, image transformation or schedule is added.
Implementation: `4953884deec25af4e9bccaf8abd4d6f976e72c05`. SSH publication
succeeded and Pages built that exact revision on 2026-11-14 at 07:34:02 UTC
(33.762 seconds). The deployed HTTP test passed all four result groups: current
version/author/14 repositories/styles, three exact original PNGs and first-step
links, archived homepage, and original notes. Browser interaction/rendering is
not claimed; first-step fragment behavior was verified from current public
initialization code.

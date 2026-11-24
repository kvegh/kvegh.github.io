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


## 2026-11-14 — CCNG laptop and mobile screenshot thumbnails

The owner requested one good-looking laptop screenshot and the mobile
screenshot on the CCNG entry as well. After visual inspection, choose the
existing public worker-workspace laptop view and mobile-overview portrait.
The laptop view presents the workspace without the coordinator warning banner.
Copy both exact original files, without editing, to local homepage assets.

Use the existing whole-image thumbnail presentation, with a compact portrait
variant and responsive wrapping beside the laptop view. Both thumbnails open
their full-size local image; CCNG has no separate interactive visualization
identified here. Retain its repository and existing screenshot links. This
extends the existing thumbnail presentation, patch version 0.1.1.

The deployed HTTP check now expects five previews and supports PNG/JPEG image
bytes. No browser, image generator, framework or scheduled task is introduced.
Original three visualization destinations remain the supported first-step URLs.
Implementation: c8bbd68bc53b5ddd99bde7cedf2347ce06ba5bfd. Pages built that exact source on 2026-11-14 at 07:50:43 UTC (39.704 seconds). The deployed HTTP test passed all four groups, including five exact original PNG/JPEG images and their intended destinations, plus catalogue/styles/archive/notes. Browser rendering remains unverified under the existing owner choice.


## 2026-11-14 — Two sections for a broader personal portfolio

The owner explicitly requested Advanced AAP usecases and Random code musings,
with top jump links and the existing understated appearance. Keep the small
author introduction while making the page's title and description about code
projects more broadly.

Move the existing CCNG entry into the second section and add the explicitly
selected Vortex Panic and Assistant Team projects. The owner confirmed all
three through the structured choice. Retain the 13 other AAP/supporting
projects and all five existing screenshot previews, destinations and original
image bytes. The owner clarified that Hetzner redeploy is not a separate
project yet; do not add it. No placeholder repositories or forks are included.

Vortex Panic is a browser-based space-travel experiment. Its public Pages
configuration confirms the existing playable page is built. Assistant Team's
public README supports the multi-agent workspace description; this does not
claim new runtime acceptance for that project.

Version 0.2.0 records this content-structure feature within the existing static
HTML/CSS design. Extend the deployed HTTP check to verify 16 projects, their
two-section placement and the top jump destinations. No new framework, service,
schedule, browser installation or remote-system access is added. Implementation: 4917fb591b3aa64c280a6216be2469877abef79b. SSH publication succeeded; Pages built this exact source from 08:01:07 to 08:01:42 UTC on 2026-11-14 (35.649 seconds). The deployed HTTP check passed all16 approved project placements, both jump links, all5 original image bytes/destinations, archive and retained notes. Test completion time was not separately captured; the successful result was collected after the 08:02:59 UTC launch observation. Browser rendering remains unverified as agreed.


## 2026-11-14 — Vortex Panic screenshot thumbnail

The owner supplied a Vortex Panic screenshot and requested the same thumbnail
size as the existing previews, clickable to view. Preserve the exact original
PNG and reuse the existing 320-pixel, whole-image thumbnail style. Clicking
opens the full-size screenshot; the separate simulation link remains available.
No image transformation, new layout or dependency is needed.

Homepage patch version 0.2.1 adds the image and extends the existing deployed
HTTP check to verify six original screenshots and their destinations. This
changes only the portfolio repository. Implementation: fd1ac9814833f15d3a8c50b84c3b7cc0fa9375b1.
GitHub Pages built this source from 17:03:42 to 17:04:17 UTC on 2026-11-14.
The deployed HTTP check passed all four groups: 16 grouped projects and styles,
six exact original image files with their destinations, archive and original
notes. Browser rendering remains unverified under the existing owner choice.


## 2026-11-15 14:11 UTC — Explain the Vortex Panic name

The owner supplied the full expansion: Vastly Overambitious Relativistic Travel
EXperience with Proportional AstroNavigation Illustrating Cosmic-insignificance,
and noted the Hitchhiker’s Guide references. Add that exact wording and case
to the existing project summary, with a brief nod to The Hitchhiker’s Guide to
the Galaxy. Keep the summary at three sentences, preserving the existing
thumbnail, repository and simulation links. Homepage patch version0.2.2 records
this text-only correction. No new layout, dependency or scheduled work is added.
Implementation: 000a82d9b9d9970ba00e8e50943d4631e3093b32. GitHub Pages
built this exact source on 2026-11-15 from 14:13:06 to 14:13:37 UTC. The
existing deployed HTTP check passed all four groups: 16 grouped projects and
styles, six exact original screenshots with their destinations, archive and
original notes. A focused HTTP check also confirmed the exact expansion and
book reference, with deployed HTML byte-identical to the committed source.
Browser appearance remains unverified under the existing owner choice.


## 2026-11-24 09:08 CET — Link the RHEL Sniperpatching walkthrough

The owner requested the missing visualization link on the homepage itself. Add
a Visualization link beside Repository in the existing RHEL Sniperpatching
entry, using the established link style and verified public walkthrough URL.
Preserve the page layout, other project entries and existing publishing setup.
Homepage patch version 0.2.3 records the missing-link correction. Extend the
existing deployed HTTP test to require the destination within the correct entry.
No browser installation is authorized; visual rendering remains unverified.
The owner subsequently supplied a screenshot to add as this entry's preview;
obtaining its original file is pending, so this release adds the link first.
Implementation: 262685c409b8c94cbe83d6e97731345cfdfd4eba. GitHub Pages run
45353837620 (pages build and deployment) completed successfully; the Pages API
records the exact implementation built from 09:10:34 to 09:11:07 CET. The
version-controlled HTTP check passed all four groups against the public site,
including the new visualization link within the correct project entry and the
six existing screenshot files. Independent read-only review found no blockers.
Screenshot addition remains awaiting the original image file; no substitute was
published.

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
commit will be recorded after it exists.

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

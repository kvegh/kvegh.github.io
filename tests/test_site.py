#!/usr/bin/env python3
"""Verify the public homepage, archive and retained notes through HTTP.

Uses Python standard-library clients so deployed checks need no test framework.
See README.md#functional-verification for scope and prerequisites.
"""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen

PROJECTS = {
    "aap_autodeploy_configascode", "aiops-selfhealing-demo",
    "disconnected-windows-patching", "RHEL-sniperpatching",
    "RHEL-ConfigAsCode", "config_exceptions_ng", "automation-orchestrator",
    "ServiceNow-ITSM-Integration", "intelligent-assistant",
    "automation_portal_setup", "Automation_Dashboard", "CMDB-for-AAP",
    "command-center-ng", "Agent_generated_code_review",
}
WINDOWS_VISUALIZATION = (
    "https://kvegh.github.io/disconnected-windows-patching/demo-with-aap/"
)


PREVIEWS = {
    "/assets/thumbnails/aap-autodeploy.png": "https://kvegh.github.io/aap_autodeploy_configascode/#separation",
    "/assets/thumbnails/aiops-selfhealing.png": "https://kvegh.github.io/aiops-selfhealing-demo/#step=1",
    "/assets/thumbnails/windows-patching.png": WINDOWS_VISUALIZATION,
}


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.images = []
        self.current_link = None
        self.styles = []
        self.ids = set()
        self.text = []
        self.articles = []
        self.current_article = None
        self.version = None
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if "id" in attributes:
            self.ids.add(attributes["id"])
        if tag == "article":
            self.current_article = []
            self.articles.append(self.current_article)
        if tag == "a" and "href" in attributes:
            self.current_link = attributes["href"]
            self.links.append(attributes["href"])
            if self.current_article is not None:
                self.current_article.append(attributes["href"])
        if tag == "img":
            self.images.append((attributes, self.current_link))
        if tag == "link" and attributes.get("rel") == "stylesheet":
            self.styles.append(attributes["href"])
        if tag == "meta" and attributes.get("name") == "site-version":
            self.version = attributes.get("content")

    def handle_endtag(self, tag):
        if tag == "a":
            self.current_link = None
        if tag == "article":
            self.current_article = None

    def handle_data(self, text):
        self.text.append(text)

    def visible_text(self):
        return " ".join(" ".join(self.text).split())


def fetch_bytes(base_url, path):
    request = Request(urljoin(base_url, path), headers={
        "User-Agent": "AAP-project-showcase-functional-test",
        "Cache-Control": "no-cache",
    })
    with urlopen(request, timeout=25) as response:
        if response.status != 200:
            raise AssertionError(f"{path}: unexpected HTTP {response.status}")
        return response.read()


def fetch(base_url, path):
    return fetch_bytes(base_url, path).decode("utf-8")


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def verify(base_url):
    version = (Path(__file__).resolve().parents[1] / "VERSION").read_text().strip()
    homepage = Page(fetch(base_url, ""))
    text = homepage.visible_text()
    require(homepage.version == version, "Published version differs from checkout VERSION")
    require(all(name in text for name in ("Karoly", "Charlie", "Vegh")), "Author name missing")
    require("Ansible Solution Architect" in text, "Author role missing")
    require(len(homepage.articles) == len(PROJECTS), "Expected 14 project entries")
    expected = {f"https://github.com/kvegh/{name}" for name in PROJECTS}
    found = []
    for links in homepage.articles:
        repositories = [link.rstrip("/") for link in links if link.rstrip("/") in expected]
        require(len(repositories) == 1, "Each project must link its own repository once")
        found.extend(repositories)
    require(set(found) == expected, "Project repositories missing or duplicated")
    require(WINDOWS_VISUALIZATION in homepage.links, "Canonical Windows visualization missing")
    require("https://kvegh.github.io/disconnected-windows-patching/" not in homepage.links,
            "Superseded Windows visualization must not appear")
    for link in homepage.links:
        if link.startswith("#"):
            require(link[1:] in homepage.ids, f"Broken section link: {link}")
    require(homepage.styles, "Stylesheet link missing")
    for style in homepage.styles:
        require(bool(fetch(base_url, style).strip()), f"Empty stylesheet: {style}")
    require(any(urlsplit(urljoin(base_url, link)).path.rstrip("/") == "/archive"
                for link in homepage.links), "Homepage archive link missing")
    print(f"PASS homepage: version {version}, author, 14 distinct projects, links and styles")

    images = {attributes.get("src"): (attributes, link) for attributes, link in homepage.images}
    require(len(homepage.images) == 3 and set(images) == set(PREVIEWS), "Expected three project thumbnails")
    for source, destination in PREVIEWS.items():
        attributes, link = images[source]
        require(link == destination, f"Incorrect first-step thumbnail destination: {source}")
        require(bool(attributes.get("alt", "").strip()), f"Missing thumbnail description: {source}")
        require(attributes.get("loading") == "lazy", f"Thumbnail should load lazily: {source}")
        data = fetch_bytes(base_url, source)
        require(data.startswith(b"\x89PNG\r\n\x1a\n"), f"Thumbnail is not a PNG: {source}")
        expected = (Path(__file__).resolve().parents[1] / source.lstrip("/")).read_bytes()
        require(data == expected, f"Published thumbnail differs from supplied screenshot: {source}")
    print("PASS thumbnails: three original screenshots, descriptions and first-step links")

    archive = Page(fetch(base_url, "archive/"))
    require("@kvegh's stuff here." in archive.visible_text(), "Old homepage text missing")
    require("kvegh.github.io" in archive.visible_text(), "Old homepage title missing")
    notes_path = "/tree/pages/SILUAIDWTLUA/"
    require(any(urlsplit(urljoin(base_url, link)).path == notes_path for link in archive.links),
            "Original notes destination missing from archive")
    print("PASS archive: original homepage content and original notes link")

    notes = Page(fetch(base_url, notes_path))
    require("Stuff I Looked Up" in notes.visible_text(), "Original notes page is not rendered")
    require("Blogger tables" in notes.visible_text(), "Original notes table missing")
    require("adding-a-new-ssh-key-to-your-github-account" in notes.visible_text()
            or any("adding-a-new-ssh-key-to-your-github-account" in link for link in notes.links),
            "Original notes reference URL missing")
    print("PASS legacy notes: original public URL, notes table and reference URL")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True, help="Authorized deployed HTTPS site URL")
    arguments = parser.parse_args()
    try:
        verify(arguments.base_url.rstrip("/") + "/")
    except Exception as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)

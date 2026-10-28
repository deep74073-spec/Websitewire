from pathlib import Path
from urllib.parse import quote
from xml.etree import ElementTree as ET
from html.parser import HTMLParser
from datetime import datetime
import shutil

BASE = "https://websitewire.co.in"
ROOT = Path(__file__).resolve().parent
SITEMAP = ROOT / "sitemap.xml"

EXCLUDED_DIRS = {
    ".git", "node_modules", "backup-before-multipage", "backup-before-tools-upgrade",
    "Websitewire", "uploads", "vendor", "__pycache__"
}

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.noindex = False
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag.lower() == "meta" and attrs.get("name", "").lower() == "robots":
            if "noindex" in attrs.get("content", "").lower():
                self.noindex = True
        if tag.lower() == "link" and "canonical" in attrs.get("rel", "").lower().split():
            self.canonical = attrs.get("href")

def excluded(path):
    rel = path.relative_to(ROOT)
    if any(part.startswith(".") or part in EXCLUDED_DIRS for part in rel.parts):
        return True
    name = path.name.lower()
    if ".backup" in name or name.startswith("backup") or ".bak" in name:
        return True
    return False

def page_url(path):
    rel = path.relative_to(ROOT)
    if rel.name.lower() == "index.html":
        rel = rel.parent
        url_path = "/" if str(rel) == "." else "/" + rel.as_posix().strip("/") + "/"
    else:
        url_path = "/" + rel.as_posix()
        url_path = url_path[:-5] if url_path.lower().endswith(".html") else url_path
    return BASE + quote(url_path, safe="/-._~")

urls = set()

for path in ROOT.rglob("*.html"):
    if excluded(path) or not path.is_file():
        continue
    try:
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
        if parser.noindex:
            continue
        url = page_url(path)
        if parser.canonical:
            canonical = parser.canonical.strip()
            if canonical.startswith(BASE + "/") or canonical == BASE:
                url = canonical
            elif canonical.startswith("http://") or canonical.startswith("https://"):
                print("Skipped non-site canonical:", path.relative_to(ROOT))
                continue
        urls.add(url)
    except Exception as e:
        print("Skipped:", path.relative_to(ROOT), "-", e)

if not urls:
    raise SystemExit("ERROR: No eligible HTML pages found; sitemap unchanged.")

if SITEMAP.exists():
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = ROOT / f"sitemap.xml.backup-{stamp}"
    shutil.copy2(SITEMAP, backup)
    print("Backup:", backup.name)

ET.register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9")
ns = "http://www.sitemaps.org/schemas/sitemap/0.9"
root = ET.Element(f"{{{ns}}}urlset")

for url in sorted(urls):
    item = ET.SubElement(root, f"{{{ns}}}url")
    ET.SubElement(item, f"{{{ns}}}loc").text = url

tree = ET.ElementTree(root)
tree.write(SITEMAP, encoding="utf-8", xml_declaration=True)

# Validate the written XML and count its URLs
checked = ET.parse(SITEMAP).getroot()
count = len(checked.findall(f"{{{ns}}}url"))
print("Sitemap updated successfully.")
print("URLs included:", count)
print("File:", SITEMAP.name)

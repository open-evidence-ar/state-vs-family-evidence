"""Full local CI simulator -- validates all 20 METH issues against source + built _site/.

Usage:
  python validate_ci.py                     # check source files only (no build needed)
  python validate_ci.py --with-build        # also run jekyll build + post-build checks
  python validate_ci.py --with-serve         # build + start local server for manual nav testing
  python validate_ci.py C:\path\to\repo      # explicit repo path
"""
import os
import sys
import re
import subprocess
import hashlib
import html.parser
from pathlib import Path
from urllib.parse import urlparse

BASE = Path(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else Path(__file__).resolve().parent
if not (BASE / "_config.yml").is_file():
    print(f"ERROR: _config.yml not found in {BASE}")
    sys.exit(2)

WITH_BUILD = "--with-build" in sys.argv
WITH_SERVE = "--with-serve" in sys.argv

PASS = []
WARN = []
FAIL = []


def result(code, meth, msg):
    (PASS if code == "PASS" else WARN if code == "WARN" else FAIL).append(f"[{code}] {meth}: {msg}")


# -- METH-001: Authors / Anonymity section ------------------------
meth = members = authors = []
has_authors = False
has_coi = False
has_funding = False
has_disavowal = False
has_pgp_ref = False

for f in sorted((BASE / "sections").glob("*.md")):
    txt = f.read_text(encoding="utf-8")
    if "autores" in txt.lower() and "anónim" in txt.lower():
        has_authors = True
    if "conflicto" in txt.lower() and ("interés" in txt.lower() or "intereses" in txt.lower()):
        has_coi = True
    if "financiamiento" in txt.lower() or "funding" in txt.lower():
        has_funding = True
    if "condenamos" in txt.lower() and "violencia" in txt.lower():
        has_disavowal = True
    if "public.pem" in txt or "public key" in txt.lower():
        has_pgp_ref = True

checks = {"Authors section": has_authors, "COI declaration": has_coi, "Funding disclosure": has_funding, "General disavowal": has_disavowal, "PGP key reference on site": has_pgp_ref}
missing = [k for k, v in checks.items() if not v]
if not missing:
    result("PASS", "METH-001", "All author/governance elements present")
else:
    result("FAIL", "METH-001", f"Missing: {', '.join(missing)}")


# -- METH-002: Domain-specific correction triggers ----------------
meth_file = (BASE / "sections" / "00-methodology.md")
meth_txt = meth_file.read_text(encoding="utf-8") if meth_file.is_file() else ""
has_specific_triggers = any(kw in meth_txt for kw in ["RNR publica", "OVG actualiza", "SNIC publica", "recalcularemos"])
if has_specific_triggers:
    result("PASS", "METH-002", "Domain-specific correction triggers present")
else:
    result("WARN", "METH-002", "Correction policy generic -- no domain-specific falsifiable triggers")


# -- METH-003: Contribution policy completeness -------------------
has_issue_template = (BASE / ".github" / "ISSUE_TEMPLATE").is_dir() and list((BASE / ".github" / "ISSUE_TEMPLATE").glob("*"))
has_pr_template = (BASE / ".github" / "PULL_REQUEST_TEMPLATE.md").is_file() or (BASE / ".github" / "PULL_REQUEST_TEMPLATE").is_dir()
has_contributing = (BASE / "CONTRIBUTING.md").is_file()
has_repo_link = "repository_url" in meth_txt or "github.com" in meth_txt

checks3 = {"Issue templates": has_issue_template, "PR template": has_pr_template, "CONTRIBUTING.md": has_contributing, "Repo link on site": has_repo_link}
missing3 = [k for k, v in checks3.items() if not v]
if not missing3:
    result("PASS", "METH-003", "Contribution policy complete")
else:
    result("FAIL", "METH-003", f"Missing: {', '.join(missing3)}")


# -- METH-004: Source archiving -----------------------------------
sources_file = BASE / "sections" / "12-sources.md"
src_txt = sources_file.read_text(encoding="utf-8") if sources_file.is_file() else ""
archive_count = len(re.findall(r'archive\.(is|today|org)|web\.archive\.org', src_txt))
url_count = len(re.findall(r'https?://[^\s\)"\]]+', src_txt))
all_section_urls = 0
all_section_archived = 0
for f in sorted((BASE / "sections").glob("*.md")):
    txt = f.read_text(encoding="utf-8")
    all_section_urls += len(re.findall(r'https?://[^\s\)"\]]+', txt))
    all_section_archived += len(re.findall(r'archive\.(is|today|org)|web\.archive\.org', txt))

if all_section_archived > 0 and all_section_archived >= all_section_urls * 0.5:
    result("PASS", "METH-004", f"{all_section_archived} archived links across sections")
elif all_section_archived > 0:
    result("WARN", "METH-004", f"Only {all_section_archived}/{all_section_urls} source URLs archived")
else:
    result("FAIL", "METH-004", f" ZERO archived links -- {all_section_urls} URLs vulnerable to link rot")


# -- METH-005: Sourcing policy specificity ------------------------
sp_file = BASE / "_includes" / "sourcing-policy.md"
sp_txt = sp_file.read_text(encoding="utf-8") if sp_file.is_file() else ""
has_non_official_flag = "no oficial" in sp_txt.lower() or "non-official" in sp_txt.lower()
has_translation_note = "idioma" in sp_txt.lower() or "traducción" in sp_txt.lower() or "translation" in sp_txt.lower()

checks5 = {"Non-official flagging": has_non_official_flag, "Translation note": has_translation_note}
missing5 = [k for k, v in checks5.items() if not v]
if not missing5:
    result("PASS", "METH-005", "Sourcing policy complete")
else:
    result("WARN", "METH-005", f"Missing: {', '.join(missing5)}")


# -- METH-006: PGP key real (not placeholder) ---------------------
pem_file = BASE / "public.pem"
pem_txt = pem_file.read_text(encoding="utf-8") if pem_file.is_file() else ""
is_placeholder = "Placeholder" in pem_txt or "TO BE GENERATED" in pem_txt or "pendiente" in pem_txt
if not is_placeholder and "BEGIN PGP" in pem_txt and pem_txt.strip().count("\n") > 3:
    result("PASS", "METH-006", "PGP key appears real")
elif is_placeholder:
    result("FAIL", "METH-006", "PGP key is PLACEHOLDER -- no cryptographic verification possible")
else:
    result("WARN", "METH-006", "PGP key present but may be incomplete or unverified")


# -- METH-007: Integrity hash generated ---------------------------
int_file = BASE / "integrity.txt"
int_txt = int_file.read_text(encoding="utf-8") if int_file.is_file() else ""
is_placeholder_int = "pendiente" in int_txt or "hash" in int_txt.lower() and len(int_txt.strip()) < 80
if not is_placeholder_int and re.search(r'[a-f0-9]{64}', int_txt):
    result("PASS", "METH-007", "Integrity hash present and looks valid")
elif is_placeholder_int:
    result("FAIL", "METH-007", "Integrity hash is PLACEHOLDER")
else:
    result("WARN", "METH-007", "Integrity file exists but hash format unclear")


# -- METH-008: Signature file -------------------------------------
sig_file = BASE / "signature"
sig_exists = sig_file.is_file() and sig_file.stat().st_size > 0
if sig_exists:
    result("PASS", "METH-008", "Signature file exists")
else:
    result("FAIL", "METH-008", "No signature file -- no authenticity verification")


# -- METH-009: Nomenclature / glossary -----------------------------
required_terms = ["NNyA", "OVD", "OVG", "RNR", "UFEM", "SNIC", "CSJN", "MPF"]
defined_terms = set()
for f in sorted((BASE / "sections").glob("*.md")):
    txt = f.read_text(encoding="utf-8")
    if "nomenclatura" in txt.lower() or "glosario" in txt.lower():
        for term in required_terms:
            pattern = rf'\*\*{re.escape(term)}\*\*[^\w\n]'
            if re.search(pattern, txt):
                defined_terms.add(term)

missing_terms = [t for t in required_terms if t not in defined_terms]
if not missing_terms:
    result("PASS", "METH-009", "All key terms defined in nomenclature/glossary")
else:
    result("FAIL", "METH-009", f"Undefined terms: {', '.join(missing_terms)} ({len(defined_terms)}/{len(required_terms)} defined)")


# -- METH-010: Counter-claims section ------------------------------
has_counter = False
for f in sorted((BASE / "sections").glob("*.md")):
    txt = f.read_text(encoding="utf-8")
    if "contra" in txt.lower() and "argumen" in txt.lower():
        has_counter = True
if has_counter:
    result("PASS", "METH-010", "Counter-claims section exists")
else:
    result("FAIL", "METH-010", "No counter-claims section -- core PE methodology missing")


# -- METH-011: Revision log ---------------------------------------
has_revisions = False
for f in sorted((BASE / "sections").glob("*.md")):
    txt = f.read_text(encoding="utf-8")
    # A proper revision log needs a section heading with "revis" AND a table with version+date columns
    if re.search(r'^##?\s+.*revis', txt, re.MULTILINE | re.IGNORECASE):
        # Look for table with at least Versi.n/Fecha headers
        if re.search(r'\|\s*Versi\w+\s*\|', txt) and re.search(r'\|\s*Fecha\s*\|', txt):
            has_revisions = True
if has_revisions:
    result("PASS", "METH-011", "Revision log present")
else:
    result("FAIL", "METH-011", "No revision/version history")


# -- METH-012: Purpose depth --------------------------------------
purpose_depth = 0
lines_after_purpose = []
capture = False
for line in meth_txt.split("\n"):
    lower_line = line.lower()
    if "prop" in lower_line and ("sito" in lower_line or "sito" in lower_line):
        capture = True
    elif capture and (line.startswith("## ") or line.startswith("---")):
        capture = False
    elif capture:
        lines_after_purpose.append(line.strip())

substantive_lines = [l for l in lines_after_purpose if l and not l.startswith("#") and l not in ("---", "")]
purpose_depth = len(substantive_lines)
if purpose_depth >= 6:
    result("PASS", "METH-012", f"Purpose section substantive ({purpose_depth} lines)")
elif purpose_depth >= 3:
    result("WARN", "METH-012", f"Purpose section thin ({purpose_depth} lines) -- PE has 6+")
else:
    result("FAIL", "METH-012", f"Purpose section too thin ({purpose_depth} lines) -- 1 sentence each vs PE's 2-3 paragraphs")


# -- METH-013: Deploy workflow order ------------------------------
deploy_file = BASE / ".github" / "workflows" / "deploy.yml"
deploy_txt = deploy_file.read_text(encoding="utf-8") if deploy_file.is_file() else ""
lines = deploy_txt.split("\n")
upload_line = None
archive_line = None
integrity_line = None
for i, line in enumerate(lines):
    if "upload-pages-artifact" in line:
        upload_line = i
    if "zip" in line and "archive" in line.lower():
        archive_line = i
    if "sha256sum" in line or "integrity" in line.lower():
        integrity_line = i

if upload_line and archive_line and integrity_line:
    if archive_line < upload_line and integrity_line < upload_line:
        result("PASS", "METH-013", "Deploy workflow: archive + integrity generated BEFORE upload")
    else:
        result("FAIL", "METH-013", f"Deploy workflow order wrong: archive@{archive_line}, integrity@{integrity_line}, upload@{upload_line}")
else:
    result("WARN", "METH-013", "Could not determine deploy workflow step order")


# -- METH-014: Mobile nav toggle ---------------------------------
layout_file = BASE / "_layouts" / "default.html"
layout_txt = layout_file.read_text(encoding="utf-8") if layout_file.is_file() else ""
has_toggle_html = "nav-toggle" in layout_txt
has_toggle_js = "nav-toggle" in layout_txt and "addEventListener" in layout_txt
has_show_css = False
css_file = BASE / "assets" / "css" / "style.scss"
css_txt = css_file.read_text(encoding="utf-8") if css_file.is_file() else ""
if ".nav-links.show" in css_txt or ".show" in css_txt:
    has_show_css = True

checks14 = {"Toggle button HTML": has_toggle_html, "Toggle JS handler": has_toggle_js, ".show CSS class": has_show_css}
missing14 = [k for k, v in checks14.items() if not v]
if not missing14:
    result("PASS", "METH-014", "Mobile nav toggle complete")
else:
    result("FAIL", "METH-014", f"Missing: {', '.join(missing14)}")


# -- METH-015: Nav anchor links ----------------------------------
nav_hrefs = re.findall(r'href=["\']#([^"\']+)["\']', layout_txt)
valid_anchors = set()

for f in sorted((BASE / "sections").glob("*.md")):
    txt = f.read_text(encoding="utf-8")
    for m in re.finditer(r'\{:?\s*#([^}]+)\}', txt):
        valid_anchors.add(m.group(1))
    for m in re.finditer(r'^#+\s+(.+)$', txt, re.MULTILINE):
        heading = m.group(1)
        anchor = heading.lower().strip()
        anchor = re.sub(r'[^\w\s-]', '', anchor)
        anchor = re.sub(r'\s+', '-', anchor)
        valid_anchors.add(anchor)

# Also scan for raw HTML id="..." attributes (e.g. <div id="secciones">)
for f in sorted((BASE / "sections").glob("*.md")) + [BASE / "index.md"]:
    txt = f.read_text(encoding="utf-8")
    for m in re.finditer(r'id=["\']([^"\']+)["\']', txt):
        valid_anchors.add(m.group(1))

broken_anchors = []
for href in nav_hrefs:
    if href not in valid_anchors:
        broken_anchors.append(f"#{href}")

if not broken_anchors:
    result("PASS", "METH-015", "All nav anchor links resolve to valid IDs")
else:
    result("FAIL", "METH-015", f"Anchor links with no matching ID: {', '.join(broken_anchors)}")


# -- METH-016: Table of Contents ----------------------------------
index_file = BASE / "index.md"
index_txt = index_file.read_text(encoding="utf-8") if index_file.is_file() else ""
has_toc = "section-toc" in index_txt or "section_toc" in index_txt
if has_toc:
    result("PASS", "METH-016", "In-page TOC present in index.md")
else:
    result("FAIL", "METH-016", "No in-page TOC -- CSS .section-toc defined but unused")


# -- METH-017: jekyll-scholar unused ------------------------------
gemfile = (BASE / "Gemfile").read_text(encoding="utf-8") if (BASE / "Gemfile").is_file() else ""
has_scholar = "jekyll-scholar" in gemfile
has_bib_dir = (BASE / "_bibliography").is_dir()
has_scholar_config = False
config_file = BASE / "_config.yml"
if config_file.is_file():
    if "scholar" in config_file.read_text(encoding="utf-8"):
        has_scholar_config = True

if not has_scholar:
    result("PASS", "METH-017", "jekyll-scholar removed from Gemfile")
elif has_scholar and not has_bib_dir and not has_scholar_config:
    result("FAIL", "METH-017", "jekyll-scholar in Gemfile but unused (no _bibliography/, no config)")
else:
    result("PASS", "METH-017", "jekyll-scholar configured and used")


# -- METH-018: Empty directories -----------------------------------
empty_dirs = []
for d in ["_data", "sources", "src/assets", "src/sections", "docs"]:
    dp = BASE / d
    if dp.is_dir() and not any(dp.iterdir()):
        empty_dirs.append(d)
if not empty_dirs:
    result("PASS", "METH-018", "No empty directories")
else:
    result("FAIL", "METH-018", f"Empty directories: {', '.join(empty_dirs)}")


# -- METH-019: validate.py hardcoded path -------------------------
val_file = BASE / "validate.py"
val_txt = val_file.read_text(encoding="utf-8") if val_file.is_file() else ""
is_hardcoded = bool(re.search(r'BASE\s*=\s*r["\']C:\\', val_txt))
if is_hardcoded:
    result("FAIL", "METH-019", "validate.py has hardcoded Windows path")
else:
    result("PASS", "METH-019", "validate.py uses relative/dynamic path")


# -- METH-020: Footer links ---------------------------------------
footer_links = re.findall(r'href=["\']{{\s*[\'"]([^\'"]+)', layout_txt)
footer_has_sig = any("signature" in l for l in footer_links)
footer_has_pem = any("public.pem" in l for l in footer_links)
footer_has_int = any("integrity" in l for l in footer_links)
footer_has_archive = any("archive.zip" in l for l in footer_links)

checks20 = {"public.pem link": footer_has_pem, "signature link": footer_has_sig, "integrity.txt link": footer_has_int, "archive.zip link": footer_has_archive}
missing20 = [k for k, v in checks20.items() if not v]
if not missing20:
    result("PASS", "METH-020", "Footer links complete (pem + signature + integrity + archive)")
else:
    result("WARN", "METH-020", f"Footer missing: {', '.join(missing20)}")


# ══════════════════════════════════════════════════════════════════
#  BUILD-SITE CHECKS  (only if --with-build)
# =============================================================
if WITH_BUILD or WITH_SERVE:
    print("\n-- Running Jekyll build --")
    build_ok = False
    try:
        ret = subprocess.run(["bundle", "exec", "jekyll", "build"], cwd=str(BASE), capture_output=True, text=True, timeout=180)
        if ret.returncode != 0:
            print(f"  BUILD FAILED:\n{ret.stderr}")
            result("FAIL", "BUILD", "Jekyll build failed")
        else:
            build_ok = True
            result("PASS", "BUILD", "Jekyll build succeeded")
    except FileNotFoundError:
        print("  bundle/jekyll not found -- skipping build checks")
        print("  Install Ruby + Bundler: https://jekyllrb.com/docs/installation/windows/")
        result("WARN", "BUILD", "Jekyll not installed -- build verification skipped")
    except Exception as e:
        print(f"  Build error: {e}")
        result("FAIL", "BUILD", f"Jekyll build error: {e}")

    if build_ok:
        site_dir = BASE / "_site"

        # Check index.html exists and has content
        idx = site_dir / "index.html"
        if idx.is_file() and idx.stat().st_size > 1000:
            idx_html = idx.read_text(encoding="utf-8")
            result("PASS", "BUILD: index.html", f"Generated ({idx.stat().st_size:,} bytes)")

            # Check all nav anchor IDs exist in built HTML
            built_ids = set(re.findall(r'id=["\']([^"\']+)["\']', idx_html))
            nav_ids_in_html = set(re.findall(r'href=["\'][^"\']*#([^"\']+)["\']', idx_html))
            missing_in_built = nav_ids_in_html - built_ids - {""}
            if not missing_in_built:
                result("PASS", "BUILD: anchors", "All anchor links resolve in built HTML")
            else:
                result("FAIL", "BUILD: anchors", f"Missing IDs in built HTML: {', '.join('#'+a for a in missing_in_built)}")

            # Check mobile nav JS present
            if "addEventListener" in idx_html and "nav-toggle" in idx_html:
                result("PASS", "BUILD: mobile-nav", "Nav toggle JS present in built HTML")
            else:
                result("FAIL", "BUILD: mobile-nav", "Nav toggle JS missing from built HTML")

        else:
            result("FAIL", "BUILD: index.html", "Not found or too small")
            idx = None

        # Generate archive.zip
        archive_ret = subprocess.run(
            ["powershell", "-Command",
             f"Compress-Archive -Path '{site_dir}/*' -DestinationPath '{site_dir / 'archive.zip'}' -Force"],
            capture_output=True, text=True
        )
        if (site_dir / "archive.zip").is_file():
            result("PASS", "BUILD: archive.zip", f"Generated ({(site_dir / 'archive.zip').stat().st_size:,} bytes)")
        else:
            result("FAIL", "BUILD: archive.zip", "Failed to generate")

        # Generate integrity.txt
        if idx and idx.is_file():
            h = hashlib.sha256(idx.read_bytes()).hexdigest()
            int_content = f"SHA256 (index.html) = {h}\n"
            (site_dir / "integrity.txt").write_text(int_content, encoding="utf-8")
            result("PASS", "BUILD: integrity.txt", f"SHA256 = {h[:16]}...")

        # Check public.pem in site
        if (site_dir / "public.pem").is_file():
            pem_s = (site_dir / "public.pem").read_text(encoding="utf-8")
            if "Placeholder" not in pem_s:
                result("PASS", "BUILD: public.pem", "Deployed and appears real")
            else:
                result("FAIL", "BUILD: public.pem", "Deployed but still PLACEHOLDER")
        else:
            result("FAIL", "BUILD: public.pem", "Not deployed")

        # Check signature
        if (site_dir / "signature").is_file():
            result("PASS", "BUILD: signature", "Present in _site/")
        else:
            result("WARN", "BUILD: signature", "Not generated -- needs GPG key setup")

        # Check for broken internal links in HTML
        if idx:
            all_hrefs = re.findall(r'href=["\']([^"\']+)["\']', idx_html)
            internal_broken = []
            for href in all_hrefs:
                if href.startswith("#") or href.startswith("{{") or href.startswith("mailto:"):
                    continue
                parsed = urlparse(href)
                if parsed.scheme in ("http", "https") and not parsed.netloc:
                    target = site_dir / parsed.path.lstrip("/")
                    if not target.is_file() and not (target / "index.html").is_file():
                        internal_broken.append(href)
            if not internal_broken:
                result("PASS", "BUILD: links", "No broken internal links in built site")
            else:
                result("FAIL", "BUILD: links", f"Broken internal links: {', '.join(internal_broken[:5])}")

    if WITH_SERVE:
        print("\n-- Starting local server --")
        print("  Run manually:  bundle exec jekyll serve")
        print("  Or:            npx serve _site")
        print("  Then open http://localhost:4000 (or :3000)")


# ══════════════════════════════════════════════════════════════════
#  REPORT
# ══════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  METHODOLOGY COMPLIANCE REPORT -- vs Project-Evidence Framework")
print("=" * 70)

if PASS:
    print(f"\n  PASS ({len(PASS)}):")
    for m in PASS:
        print(f"    {m}")

if WARN:
    print(f"\n  WARN ({len(WARN)}):")
    for m in WARN:
        print(f"    {m}")

if FAIL:
    print(f"\n  FAIL ({len(FAIL)}):")
    for m in FAIL:
        print(f"    {m}")

total = len(PASS) + len(WARN) + len(FAIL)
print(f"\n{'-' * 70}")
print(f"  Total: {total} checks | {len(PASS)} PASS | {len(WARN)} WARN | {len(FAIL)} FAIL")
if FAIL:
    print(f"  >>> {len(FAIL)} issues must be fixed before deployment <<<")
    sys.exit(1)
elif WARN:
    print(f"  >>> {len(WARN)} warnings -- recommended but not blocking <<<")
    sys.exit(0)
else:
    print("  All methodology checks PASSED")
    sys.exit(0)

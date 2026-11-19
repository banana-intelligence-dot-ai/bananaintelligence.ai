#!/usr/bin/env python3
"""Check the generated Markdown against the HTML pages and the repo.

1. Every sentence in each .md appears in its page (visible text plus image alt text).
2. Every sentence of the page's main content appears in its .md (nothing dropped),
   apart from the interactive games on the home page, which are skipped on purpose.
3. Every internal link in the .md points at a file that exists in the repo.
"""
import html
import os
import re
import sys

import importlib.util

spec = importlib.util.spec_from_file_location("bm", os.path.join(os.path.dirname(os.path.abspath(__file__)), "build-markdown.py"))
bm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bm)

ROOT = bm.ROOT
nospace = lambda s: re.sub(r"\s+", "", html.unescape(s).replace(" ", " "))


def html_text(rel):
    """Visible text of the whole page by plain tag stripping (independent of the converter), plus alt text."""
    t = open(os.path.join(ROOT, rel, "index.html"), encoding="utf-8").read()
    alts = " ".join(re.findall(r'alt="([^"]+)"', t))
    t = re.sub(r"<(script|style|svg)\b.*?</\1>", " ", t, flags=re.S)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    return nospace(re.sub(r"<[^>]+>", "", t) + alts)


def block_text(n):
    """Like the converter's plain(), but breaks lines at block elements so sentences do not run together."""
    if isinstance(n, str):
        return n
    if bm.skipped(n):
        return ""
    inner = "".join(block_text(k) for k in n.kids)
    return inner if n.tag in bm.INLINE_TAGS - {"span", "time"} else "\n" + inner + "\n"


def md_plain(md):
    md = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", md)
    md = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)
    md = re.sub(r"^(#+ |- |\d+\. )", "", md, flags=re.M)
    md = md.replace("**", "").replace("`", "")
    md = re.sub(r"(?<!\\)\*([^*\n]+)\*", r"\1", md)  # single-star emphasis
    return re.sub(r"\\([\\*_\[\]<>])", r"\1", md)


def fragments(s):
    out = []
    for line in s.split("\n"):
        for part in line.split(" · "):
            out += [p for p in re.split(r"(?<=[.!?])\s+", part) if p.strip()]
    return out


bad = 0
for rel in bm.PAGES:
    md = open(os.path.join(ROOT, rel, "index.md"), encoding="utf-8").read()
    ht = html_text(rel)
    lines = md.split("\n")
    body = "\n".join(lines[3:])  # skip H1 and canonical URL line
    plain = md_plain(body)
    n = 0
    for f in fragments(plain):
        n += 1
        if nospace(f) not in ht:
            bad += 1
            print("MD NOT IN HTML [%s]: %s" % (rel or "/", f))
    # reverse: page sentences missing from the md
    tree = bm.Tree()
    tree.feed(open(os.path.join(ROOT, rel, "index.html"), encoding="utf-8").read())
    main = bm.find(bm.find(tree.root, "body"), "main")
    vis = html.unescape(block_text(main)).replace("\u00a0", " ")
    mdn = nospace(md_plain(md))
    for f in fragments(vis):
        if f.strip() and not f.strip().isdigit() and nospace(f) not in mdn:  # bare digits: wall numbering badges
            bad += 1
            print("HTML NOT IN MD [%s]: %s" % (rel or "/", f.strip()))
    for url in re.findall(r"\]\((https://bananaintelligence\.ai[^)]*)\)", md):
        p = url[len(bm.SITE):].split("?")[0].split("#")[0]
        fs = os.path.join(ROOT, p.lstrip("/"))
        if not (os.path.isfile(fs) or os.path.isfile(os.path.join(fs, "index.html"))):
            bad += 1
            print("BROKEN LINK [%s]: %s" % (rel or "/", url))
    print("ok %-40s %d sentences" % (rel or "/", n))
# The routing file serves these pages as Markdown. Its list must match the generator's.
mw = open(os.path.join(ROOT, "middleware.js"), encoding="utf-8").read()
mw_pages = re.findall(r'^  "(/[^"]*)",$', mw, flags=re.M)
if mw_pages != ["/" + rel for rel in bm.PAGES]:
    bad += 1
    print("PAGE LISTS DIFFER: middleware.js", mw_pages, "vs build-markdown.py", bm.PAGES)
print("misses:", bad)
sys.exit(1 if bad else 0)

#!/usr/bin/env python3
"""Generate a plain Markdown copy of each main page, beside its index.html.

Usage: python3 tools/build-markdown.py   (run from anywhere; it works from the repo root)

Rules: same words as the page. Visible main content only, plus the footer's contact line.
Skipped: nav, scripts, styles, svg, canvas, buttons, screen-reader-only text, decorative
elements, and the interactive games on the home page. Output is never hand-edited:
change a page, run this, commit both.
"""
import html.parser
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://bananaintelligence.ai"
PAGES = [
    "",
    "how-we-build/",
    "how-we-build/one-person-many-apps/",
    "what-we-make/",
    "what-we-make/louie/",
    "what-we-make/daystart/",
    "what-we-make/artifact-news/",
    "what-we-make/my-happenings/",
    "what-we-make/plain-ballot/",
    "what-we-make/politicians-by-jev/",
    "what-we-make/spooky-particles/",
    "releases/",
]

VOID = {"br", "img", "hr", "meta", "link", "input", "source", "wbr"}
SKIP_TAGS = {"script", "style", "svg", "canvas", "button", "nav", "noscript", "template", "details"}
SKIP_CLASS = {"sr", "tape"}
INLINE_TAGS = {"a", "b", "strong", "em", "i", "code", "span", "time", "img", "br", "small", "mark", "u"}
PIECE_TAGS = {"b", "strong", "span", "p", "div"}


class Node:
    def __init__(self, tag, attrs, parent=None):
        self.tag, self.attrs, self.parent, self.kids = tag, dict(attrs), parent, []

    def classes(self):
        return set((self.attrs.get("class") or "").split())


class Tree(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root", [])
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.kids.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.kids.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.kids.append(data)


def find(node, tag):
    for k in node.kids:
        if isinstance(k, Node):
            if k.tag == tag:
                return k
            r = find(k, tag)
            if r:
                return r
    return None


def skipped(n):
    return (
        n.tag in SKIP_TAGS
        or n.classes() & SKIP_CLASS
        or n.attrs.get("aria-hidden") == "true"
        or "hidden" in n.attrs
    )


def absurl(u):
    if u.startswith("/"):
        return SITE + u
    return u


def esc(s):
    return re.sub(r"([\\*_\[\]<>])", r"\\\1", s)


def squash(s):
    return re.sub(r"\s+", " ", s.replace(" ", " "))


def inline(n):
    if isinstance(n, str):
        return esc(squash(n))
    if skipped(n):
        return ""
    t = n.tag
    inner = "".join(inline(k) for k in n.kids)
    if t == "br":
        return " "
    if t == "img":
        alt = squash(n.attrs.get("alt") or "").strip()
        return "![%s](%s)" % (alt, absurl(n.attrs.get("src", ""))) if alt else ""
    if t == "a":
        href = n.attrs.get("href", "")
        txt = inner.strip()
        if not txt:
            return ""
        if href.startswith("#"):
            return inner
        return "[%s](%s)" % (txt, absurl(href))
    if t in ("b", "strong"):
        return "**%s**" % inner.strip() if inner.strip() else ""
    if t in ("em", "i"):
        return "*%s*" % inner.strip() if inner.strip() else ""
    if t == "code":
        return "`%s`" % squash("".join(plain(k) for k in n.kids)).strip()
    return inner


def plain(n):
    if isinstance(n, str):
        return n
    return "" if skipped(n) else "".join(plain(k) for k in n.kids)


def clean(s):
    return re.sub(r" +", " ", s).strip()


def text_of(n):
    return clean(inline(n))


def list_item(li):
    elems = [k for k in li.kids if isinstance(k, Node) and not skipped(k)]
    if any(e.tag in PIECE_TAGS for e in elems):
        pieces, run = [], []
        for k in li.kids:
            if isinstance(k, Node) and k.tag in PIECE_TAGS:
                if clean("".join(run)):
                    pieces.append(clean("".join(run)))
                run = []
                if not skipped(k) and text_of(k):
                    pieces.append(text_of(k))
            else:
                run.append(inline(k))
        if clean("".join(run)):
            pieces.append(clean("".join(run)))
        return pieces
    return [text_of(li)]


def wall_item(a):
    def by_class(n, c):
        for k in n.kids:
            if isinstance(k, Node):
                if c in k.classes():
                    return k
                r = by_class(k, c)
                if r:
                    return r
        return None

    name = text_of(find(a, "b"))
    line = text_of(by_class(a, "line"))
    img = find(a, "img")
    out = "- [%s](%s)\n  %s" % (name, absurl(a.attrs["href"]), line)
    alt = squash((img.attrs.get("alt") if img else "") or "").strip()
    if alt:
        out += "\n  ![%s](%s)" % (alt, absurl(img.attrs["src"]))
    return out


def blocks(node, out):
    buf = []

    def flush():
        s = clean("".join(buf))
        buf.clear()
        if s:
            out.append(s)

    for k in node.kids:
        if isinstance(k, str):
            buf.append(inline(k))
            continue
        if skipped(k):
            continue
        t = k.tag
        if t == "a" and "pc" in k.classes():
            flush()
            out.append(wall_item(k))
        elif t in INLINE_TAGS:
            buf.append(inline(k))
        else:
            flush()
            if re.fullmatch(r"h[1-6]", t):
                s = text_of(k)
                if s:
                    out.append("#" * int(t[1]) + " " + s)
            elif t == "p":
                if "when" in k.classes():
                    parts = [text_of(c) for c in k.kids if isinstance(c, Node) and not skipped(c)]
                    s = " · ".join(p for p in parts if p)
                else:
                    s = text_of(k)
                if s:
                    out.append(s)
            elif t in ("ul", "ol"):
                items = []
                for i, li in enumerate([c for c in k.kids if isinstance(c, Node) and c.tag == "li"], 1):
                    if "entry" in li.classes():
                        blocks(li, out)
                        continue
                    pieces = [p for p in list_item(li) if p]
                    if not pieces:
                        continue
                    mark = "%d. " % i if t == "ol" else "- "
                    items.append(mark + ("\n" + " " * len(mark)).join(pieces))
                if items:
                    out.append("\n".join(items))
            else:
                blocks(k, out)
    flush()


def build(rel):
    path = os.path.join(ROOT, rel, "index.html")
    tree = Tree()
    tree.feed(open(path, encoding="utf-8").read())
    body = find(tree.root, "body")
    main = find(body, "main")
    h1 = find(main, "h1")
    title = text_of(h1)
    h1.attrs["hidden"] = ""  # emitted once, at the top
    out = []
    blocks(main, out)
    footer = find(body, "footer")
    for sp in footer.kids:
        if isinstance(sp, Node) and text_of(sp).startswith("Contact"):
            out.append(text_of(sp))
    head = "# %s\n\n%s/%s" % (title, SITE, rel)
    return head + "\n\n" + "\n\n".join(out) + "\n"


def main():
    for rel in PAGES:
        dest = os.path.join(ROOT, rel, "index.md")
        with open(dest, "w", encoding="utf-8") as f:
            f.write(build(rel))
        print("wrote", os.path.relpath(dest, ROOT))


if __name__ == "__main__":
    sys.exit(main())

# CLAUDE.md

## Project: bananaintelligence.ai

Static single-page landing site for Banana Intelligence — points visitors at our apps (MyHappenings, DayStart AI) and a contact email. No framework, no build step, no bundler. Deployed on Vercel from `main`.

### Files that matter

- `index.html` — the entire site, including inline CSS and JS
- `og.png` — social preview image, referenced from the meta tags
- `robots.txt`, `sitemap.xml` — at the repo root
- No `package.json`, no `node_modules`, no build configuration

### Brand

- **Voice:** playful, indie, sparse. *"The intelligence Apple forgot to ship."* / *"We don't ship features. We grow bananas."* Banana metaphors land; corporate copy doesn't.
- **Type:** Fraunces variable serif for display (uses `opsz` and `SOFT` axes), system sans for body.
- **Palette:** banana `#ffd60a`, deeper banana `#f7b801`, sunrise `#ffb86b`, cream paper `#fff8e1`, peel `#5a3a00`, ink `#1a1407`.
- **Texture:** subtle SVG noise overlay (paper grain, ~18% opacity, `mix-blend-mode: multiply`).
- **Motion:** the banana mark sways and spills on interaction. Respect `prefers-reduced-motion` — all animations should have a disabled state under it.

### Don't change without intent

- The brand palette and font choices
- The single-file structure (`index.html` holds CSS + JS inline on purpose)
- The "intelligence Apple forgot to ship" tagline
- The three card structure (MyHappenings, DayStart AI, Contact)

### Deployment

Vercel serves `index.html` from the repo root — no build command. DNS: apex and `www.` point at Vercel via `cname.vercel-dns.com` / `76.76.21.21`. The canonical URL is the apex (`https://bananaintelligence.ai/`).

---

# Behavioral guidelines

Derived from [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) — common LLM coding pitfalls to avoid.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

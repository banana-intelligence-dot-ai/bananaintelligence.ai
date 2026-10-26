# CLAUDE.md

## Response style (user preference)

Every response to Nate must:

- **Be succinct.** No throat-clearing, no recap of the request, no "great question." Get to the point and stop.
- **End with a TL;DR** — a short bulleted list of what just happened or what was decided.
- **End with an Actions Needed** — a short bulleted list of what Nate needs to do next. If nothing is needed, say "None" — don't omit the section.

These two lists go at the very end of the response, in that order. Skip them only for trivially short replies (a single sentence answer to a yes/no question).

## Skill usage

- **Design / UI / visual tasks** → invoke the `frontend-design:frontend-design` skill (e.g., `/frontend-design:frontend-design`). This covers: building or revising components, pages, or layouts; typography, color, and motion choices; design critiques and recommendations; anything where the deliverable is a visual interface.
- Don't reach for the skill on trivial copy edits, single-line CSS tweaks, or content-only changes — judgment applies.
- **Before any deploy** → run the `code-review` skill (e.g., `/code-review`) on the pending diff first. Surface findings to Nate before pushing the deploy. Applies to: `vercel:deploy`, `vercel deploy` from CLI, promoting a preview to production, or any action whose effect is to ship the current code to a live environment. Doesn't apply to a normal `git push` to `main` unless that push is the deploy trigger (which it currently is for this repo — pushing to `main` triggers a Vercel production deploy, so treat a push to `main` as a deploy).

## Project: bananaintelligence.ai

Static single-page site for Banana Intelligence, Nate Peace's studio for personal media and tools. Shows the public lineup (DayStart and Plain Ballot live, My Happenings coming soon), the studio note, and a contact email. No framework, no build step, no bundler. Deployed on Vercel from `main`.

### Files that matter

- `index.html` — the entire site, including inline CSS and JS
- `og.png` — 1200x630 social preview image, referenced from the meta tags
- `404.html` — branded not-found page (Vercel serves it automatically)
- `icon.svg`, `favicon.ico`, `apple-touch-icon.png`, `icon-512.png` — favicon set from the BI monogram
- `media/` — real product screens (light and dark) used in the product rows
- `robots.txt`, `sitemap.xml` — at the repo root
- No `package.json`, no `node_modules`, no build configuration

### Brand

Follows the `taste` skill's house standard (Banana Intelligence row). Refreshed 2026-10-26.

- **Voice:** Nate's voice (`nate-speak`): calm, specific, no hype, no em dashes, no exclamation marks. The line is "What was once exclusive to the elites, now for everyone." (Nate, 2026-10-26)
- **Type:** Fraunces upright for headings (optical size pinned to 144), Hanken Grotesk for everything else. Two families only.
- **Palette:** banana `#FFD23F` as the one accent (shared with DayStart). Warm off-white paper `#FBF8F0` and ink `#1A1407` in light; `#12100B` and `#F4EFE3` in dark.
- **Signature:** the brushed banana card made out to "EVERYONE" in the hero. It is the only reactive light surface on the page: a pointer-tracked highlight and up to 3 degrees of tilt on fine pointers, off under Reduce Motion and on touch.
- **Lineup:** only DayStart, Plain Ballot, and My Happenings are public. Don't name unannounced projects anywhere (copy, metadata, alt text, comments, sitemap). SupportGrid is a separate company and stays off.

### Don't change without intent

- The palette, the two font families, and the one-accent rule
- The single-file structure (`index.html` holds CSS + JS inline on purpose)
- The public lineup above
- The `daystart/` folder and its `vercel.json` routing (serves daystart.bananaintelligence.ai)

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

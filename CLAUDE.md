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
- **SEO check before every push to main:** run `npx -y seolint@1.1.1` in the repo root (config in `seolint.config.mjs`). Errors must be zero; fix warnings when they are real. Links to folder pages end with a slash (`/releases/`), and so do canonicals and the sitemap.
- **Before any deploy** → run the `code-review` skill (e.g., `/code-review`) on the pending diff first. Surface findings to Nate before pushing the deploy. Applies to: `vercel:deploy`, `vercel deploy` from CLI, promoting a preview to production, or any action whose effect is to ship the current code to a live environment. Doesn't apply to a normal `git push` to `main` unless that push is the deploy trigger (which it currently is for this repo — pushing to `main` triggers a Vercel production deploy, so treat a push to `main` as a deploy).

## Project: bananaintelligence.ai

Static single-page site for Banana Intelligence, Nate Peace's studio for personal media and tools. An app studio page: the hero, a wall of real screens from every public app, one card per app (icon, one line, one real proof point, an honest status), the studio note, and a contact email. No framework, no build step, no bundler. Deployed on Vercel from `main`.

### Files that matter

- `index.html` — the entire site, including inline CSS and JS
- `og.png` — 1200x630 social preview image, referenced from the meta tags
- `404.html` — branded not-found page (Vercel serves it automatically)
- `icon.svg`, `favicon.ico`, `apple-touch-icon.png`, `icon-512.png` — favicon set from the BI monogram
- `media/wall/` — real screens (light and dark) for the scrolling wall under the hero; `media/apps/` — each app's icon for its card. Fresh captures of the live sites plus DayStart iPhone screens; never mockups
- `robots.txt`, `sitemap.xml` — at the repo root
- No `package.json`, no `node_modules`, no build configuration

### Brand

Follows the `taste` skill's house standard (Banana Intelligence row). Refreshed 2026-10-26.

- **Voice:** Nate's voice (`nate-speak`): calm, specific, no hype, no em dashes, no exclamation marks. The motto is "Excellence. For everyone." (Nate, 2026-11-02; replaces the Oct 26 "What was once exclusive to the elites" line)
- **Type:** Hanken Grotesk only, headings included (sans since 2026-11-11). No serif.
- **Palette:** banana `#FFD23F` as the one accent (shared with DayStart). Warm off-white paper `#FBF8F0` and ink `#1A1407` in light; `#12100B` and `#F4EFE3` in dark.
- **Signature:** the wall. Three rows of real product screens under the hero, drifting slowly in opposite directions (like Nate's X banner), pausing on hover and focus, a static grid under Reduce Motion. (Nate, 2026-11-11: "let's overwhelm them with what we're building." It replaced the DayStart ready-screen card and its pointer light.)
- **Lineup (2026-11-11, app studio):** DayStart, Plain Ballot, Artifact News, Spooky Particles, Politicians by Jev (Live), My Happenings (Beta). Jev is live but not in active development (Nate, Nov 11); show it as Live. natepeace.com may appear on the wall as Nate's site. The hero's "N apps live" counts every app not paused; keep it true when a status changes. Don't name unannounced or private projects anywhere (copy, metadata, alt text, comments, sitemap), and nothing about trading. SupportGrid is a separate company and stays off.

### Don't change without intent

- The palette, the one font family, and the one-accent rule
- The single-file structure (`index.html` holds CSS + JS inline on purpose)
- The public lineup above, and the real-screens-only rule for the wall
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

## 3. Own the Codebase

**This codebase is yours: what it's for and how it's built are your call, and you'll keep building on it.**

(Nate, 2026-11-10. This replaces the old "Surgical Changes" rule.)

When a task takes you into an area:
- Merge duplicate code you find there instead of bolting a new copy on.
- Fix related bugs you find there instead of only mentioning them.
- Remove dead code in that area: imports, variables and functions nothing uses.
- Match the existing style, unless you are deliberately changing it across the whole area.

Keep it easy to check:
- Put each cleanup in its own commit, separate from the task's change, with tests passing before and after.
- Stay in the area the task touches. A problem somewhere else gets a line in the roadmap, not a detour.

The test: the area you worked in is simpler and more correct than you found it, and every commit says why.

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

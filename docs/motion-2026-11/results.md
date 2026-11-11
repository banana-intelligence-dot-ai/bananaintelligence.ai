# Motion test results (Nov 11, 2026)

Hypothesis: we lose to Greptile, Wispr Flow and Spade on motion and on one sharp idea.

Method: each critic (Opus, blind) got four pages, A to D: a still at 4 s and a 12-frame sheet from a screen recording (hero for 4 s, then a scroll of 3.5 screens). Names swapped to a made-up studio. Pass rule: ours not last and not named agent-made in 2 of 3 sets. Stop on 2 stalls. Recorder: `scripts/record.py`; set builder: `scripts/blindsets.py`.

| Round | Ours (3 sets) | Rank | Named agent-made | Wispr | Greptile | Spade |
|---|---|---|---|---|---|---|
| 1 | 5.5, 6, 6 | last x3 | 3 of 3 (about 85%) | 8.5 to 9 | 7.5 to 8.5 | 7.5 to 8 |
| 2 | 6, 6, 5.5 | last x3 | 3 of 3 | 8.5 to 9 | 8 to 8.5 | 7.5 to 8 |
| 3 | 6.5, 6, 6 | last x3 | 3 of 3 (85%) | 8.5 to 9 | 8 to 8.5 | 7.5 to 8 |

Rounds 2 and 3 are the two stalls. The test stopped there.

## Was motion the gap?

Partly. Motion moved us about half a point (5.8 to 6.2 on average) and the critics now call the idea "real" and "half an idea". What still separates us, in all nine critiques:

1. **The motion is not the product working.** Wispr corrects a word live; Spade enriches a transaction; Greptile's lizard hunts a bug. Our sun rises and the rays stream, but the critics read the rays as texture, not as "we read it all".
2. **The idea stops at the hero.** Every reference carries its idea through the scroll. Ours turns into cards and a three-up row.
3. **Made art versus generated fill.** Critics name repeated procedural text as the agent tell, every round.
4. **Proof.** No logos, no real quotes, no real numbers. We cannot invent these.
5. **Rays still run behind the lede** at the 4 s still (`shots/hero-light.jpg`). A known flaw, left as is when the test stopped.

## Files

- Hero loop: `hero.mp4` (0.68 MB), `hero.webm` (0.89 MB), 5 s at 1280 px.
- Stills: `shots/hero-light.jpg`, `shots/hero-dark.jpg`, `shots/hero-390.jpg`, `shots/poster-reduced.jpg` (reduced motion).
- Full scroll recording: `shots/scroll-light.mp4`; frame sheets `shots/frames-light.jpg`, `shots/frames-dark.jpg`.
- Each round as the critics saw it (names swapped): `rounds/r1..r3-still.jpg`, `rounds/r1..r3-frames.jpg`.
- References: `ref/`.

## Second try: the hero as a live product demo (rounds 4 and 5)

Hero = option B ("Read for you, every morning."), built to do the product's job on today's real front pages from the shared newsroom feed: a highlighter (strokes made with ChatGPT image generation through Codex) marks three real headlines, and each marked line lifts, word for word, into a DayStart briefing that then plays. Below the fold each product repeats the act on its own real line. Every number comes from the feed. Same method, same references.

| Round | Ours (3 sets) | Rank | Named agent-made | Wispr | Greptile | Spade |
|---|---|---|---|---|---|---|
| 4 | 6, 6.5, 6.5 | last x3 | 3 of 3 (75 to 90%) | 9 | 8.5 | 8 |
| 5 | 6.5, 6, 6 | last x3 | 3 of 3 (85%) | 9 | 8.5 | 8 |

Rounds 4 and 5 are the two stalls; the test stopped there. Between them: no font reflow, settled by about 3 s, the card never shows empty rows or covers the page, the triplet became one marked line of live counts.

What changed the critics' minds: all six now call the idea right ("the right idea", "a good idea, poorly run"), and they read the highlight-to-briefing step as the product working.

What did not: the hero is still "two UI cards, not art". Every reference owns one made visual (Wispr's text ribbon, Greptile's halftone lizard, Spade's engraved coin) and ours is product UI. Their shared fix: one large, physical asset (a stack of real front pages with the marker across it) with the briefing as a small second element. Smaller notes, fixed after round 5 but not re-tested: cut-off outlet names, faint unmarked rows, near-duplicate headlines, a dark lineup band that showed empty before its content arrived.

After round 5 the type moved to sans serif (Nate, Nov 11), matching main's bi-sans.

Evidence: `rounds/r4-*.jpg`, `rounds/r5-*.jpg`. The sunrise version is tag `bi-motion-v1`.

## Third try: one made image (round 6), and what each step was worth

Hero = copy plus one large linocut of a stack of front pages with invented mastheads, made with ChatGPT image generation through Codex (five techniques tried: engraving, risograph, linocut, pen and ink, cut paper; options in `rounds/r6-image-options.jpg`). Its stroke is drawn on load. The live demo became a band right below. Sans type throughout.

| Round | Ours (3 sets) | Rank | Named agent-made | Wispr | Greptile | Spade |
|---|---|---|---|---|---|---|
| 6 | 6, 6, 6 | last x3 | 3 of 3 (85%) | 9 | 8.5 | 7.5 to 8 |

Still last, so the test stopped here, per the stop rule.

What each step was worth (average of ours across the 3 sets; references stayed at 7.5 to 9 throughout):

| Step | Avg | Worth |
|---|---|---|
| Rounds 1 to 3: GSAP motion on a texture (sunrise) | 6.0 | About +0.4 over no motion. Critics: "texture, not the product working". |
| Round 4: hero as a live demo on today's real headlines | 6.3 | The only step that changed minds: every critic since calls the idea right. |
| Round 5: polish (no font jump, faster, no empty rows) | 6.2 | Zero on score; it removed the execution complaints, which left "two UI cards, not art". |
| Round 6: one made image, sans type, demo moved below | 6.0 | Negative. The image read as AI-made (invented mastheads, smudged hatching, a faint box behind it), and moving the demo out of the hero cost the "product working" credit: critics called the motion decoration again. They also flagged the headline as small (about 64 px against 100 px and up) and the highlighter used in too many places. |

Conclusion: an agent can now make the right idea and clean execution, but not, so far, an asset these critics accept as made by hand. The live demo is the strongest thing we have; if we ship anything from this branch, keep the demo in the hero (round 5) with the sans type, and commission the one image from a person.

Evidence: `rounds/r6-*.jpg` (desktop and 390 px stills, frames). Earlier versions: tag `bi-motion-v1` (sunrise), commit c14c011 (round 5 hero in sans).

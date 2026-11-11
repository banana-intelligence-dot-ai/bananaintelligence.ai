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

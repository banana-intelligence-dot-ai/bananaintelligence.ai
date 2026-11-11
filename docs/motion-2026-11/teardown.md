# Motion teardown: Greptile, Wispr Flow, Spade

Nov 11, 2026. Opened in the built-in browser at 1440 x 900 (library probe, scroll probe), then recorded the same way with `scripts/record.py`: 4 s on the hero while the pointer drifts across it, then a smooth wheel scroll down 3.5 screens. Recordings and time-stamped frame sheets: `ref/<site>.mp4`, `ref/<site>-frames.jpg`.

## What each one moves

| | Greptile | Wispr Flow | Spade |
|---|---|---|---|
| Stack (measured) | Next.js, CSS keyframes, two canvases (792 px hero, 1440 px band) | Webflow, GSAP 3.15 + ScrollTrigger (4 triggers), 2 Lottie | Rive (12 `.riv` refs), one canvas per scene, one mp4 |
| Load (0 to 1 s) | Headline and lede fade up, 600 and 700 ms, linear-ish | Nothing staged. The ribbon is already flowing at first paint | Headline is static. Empty space waits for the art |
| The hero object | A stippled lizard resolves from noise between 1.5 and 2.5 s, then a small fly buzzes round it forever | A ribbon of spoken words runs along a curved path into a voice pill. A wrong word ("their") lifts above the line and flips to "they're"; a "Grammar corrected" chip appears | An engraved coin assembles at about 2 s; transaction labels pop in; the amount ticks ($11.42 to $14.00) |
| Ambient loop | Yes: the fly, a 40 s floating sphere | Yes: the ribbon never stops | Yes: amounts keep changing |
| Pointer | No pointer effect seen on the hero | None on the hero; hover states only | None on the hero |
| Scroll | Header turns dark over dark sections. Section labels decode from glyph noise ("[ PE\|8>( ]" to a word). Step cards carry their own small canvases | One section pinned for about 6,000 px (a story steps through three states). A dark green sheet slides up over the cream with a rounded top edge. A photo card scales down as you scroll (scrub 1.5) | A dark panel holds one sentence, then turns lighter while transaction chips drift in around it. A JSON window and a card with a live amount follow |
| Durations | 600 to 700 ms for text; 1 s for the art resolve | 220 to 320 ms per letter or chip; long scrubs | About 1 s for the coin; chips on 300 to 500 ms |

## The pattern, across all three

1. **The hero motion is the product doing its job.** Wispr corrects a word. Spade enriches a transaction. Greptile's lizard hunts a bug (the fly). None of them animates decoration. This is the "one sharp idea" and the motion together; you cannot separate them.
2. **It starts late and never stops.** The object arrives 1.5 to 2.5 s after paint, after the headline has been read, and then loops quietly. The page is never fully still in the first screen.
3. **The headline does not dance.** At most a short fade up. Type stays calm; the object moves.
4. **Scroll moves panels, not paragraphs.** Sheets slide over sheets, a panel changes color, a card scales, a section pins and steps. No one uses the uniform fade-up-on-every-block pattern.
5. **Pointer reaction is rare.** None of the three uses it on the hero. It is a free edge for us (the house already owns the pointer light).
6. **Small labels move with craft.** Glyph decode (Greptile), chip pops (Wispr, Spade), ticking numbers (Spade). Mono labels plus a live number reads as "real system".

## What this means for us

- Our page loses on motion: zero things move in the first screen, and the house rule says "nothing else on the page moves". Every reference has an ambient loop.
- The fix is not "add animation". It is: make the hero object show the product's verb (reading everything, then handing you the few things that matter), arrive after the headline, and keep living quietly.
- Scroll choreography should move whole panels with intent, and the one pointer effect should stay ours.

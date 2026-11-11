# Art direction: Banana Intelligence

Read this first before any visual work on bananaintelligence.ai. Branch `bi-art`, Nov 11, 2026.

```
Brand:       Banana Intelligence. Build for the elites, share with everyone.
One belief:  Someone has already read everything and set out only what matters, for me.
Asset:       Live product moment, drawn. A silver valet's tray set out at dawn: the phone
             playing DayStart's briefing (yellow play button, waveform), a newspaper with one
             chart (Artifact News), a ballot card with one box ticked (Plain Ballot), coffee.
             The butler's tray is the elite assistant; what sits on it is the products.
Technique:   Copperplate line engraving, banknote grade. Ink lines follow the form and swell
             in shadow, cross-hatching in the darks, stipple on soft surfaces. Two-plate print:
             ink plus one engraved banana-yellow element (the play button), slightly off register.
Why only us: The tray is the "assistant who reads everything first"; the play button is
             DayStart's real one. Engraving is how elite things were printed (banknotes),
             here spent on an everyday morning. The motto as a picture.
Palette:     paper #FBF8F0, ink #1A1407, banana #FFD23F (play button and the one CTA), warm ink tints.
             Dark: paper #12100B, ink #F4EFE3, the plate reprinted as its night edition.
Type:        Fraunces upright, opsz 144, 92 px at 1440 (clamp 72 to 96), tracking -0.02em;
             Hanken Grotesk body. The headline sits on clear paper; it never touches the tray.
Echoes:      1) three spot engravings on the how-it-works steps, same plate, same light;
             2) the hero CTA is the play button's yellow; 3) the yellow play button
             returns as the real DayStart ready screen in the lineup. Share image: not done yet.
Motion:      Low morning light follows the pointer across the plate (fine pointers only).
             Still plate under Reduce Motion and on touch.
Voice:       plain, warm, exact. "We read everything first and set out what matters."
Never:       a cartoon banana or any mascot; a second accent color or a gradient sky.
```

## How the plate was made

ChatGPT image generation through the Codex CLI (`codex exec -m gpt-5.6-sol`, image_generation feature), on Nate's ChatGPT plan. 23 images, no failures, 52 to 102 seconds each (about 70 typical). Three directions, three images each: A, a photographed tray; B, a tall stack of everything read with one card on top; C, this engraving. C won: it is the only one that owns a technique (A read as a stock phone mockup, B as an abstract shelf), and its yellow button is the product. Round 2 (D) redrew C with the three products on the tray and an engraved yellow, using C2 as a style reference; D3 shipped. The dark plate is a Codex image edit of D3 ("night edition"), not an inverted file. Thumbnails in `docs/art-2026-11/directions/`.

Blind test (3 Opus critics, ours among Greptile, Wispr Flow, Spade): last in all 3 sets in every round, named as agent-made every time. R1 7.3, 7.3, 7.1; R2 7.3, 7.3, 7.2; R3 6.8, 7.6, 7.1. Critics' repeated reasons: the props read as a literal list of features, generated hatching has no hierarchy of detail, a generic headline, and thin chrome around the hero.

Post: channel gains so the paper lands on #FBF8F0, Lanczos upscale to 2400 px with a light unsharp, paper noise flattened above 92% luminance, cwebp q72 at 1200, 1800 and 2400 wide.

Prompt for the chosen plate: `docs/art-2026-11/prompt-light.txt` (run with C2 attached). Night edition: `prompt-dark.txt`. Round 1 engraving prompt: `prompt-round1-C.txt`.

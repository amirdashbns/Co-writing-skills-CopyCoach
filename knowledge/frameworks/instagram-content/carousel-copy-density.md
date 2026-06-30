# Carousel Copy Density — Amir's Voice on Slides

Reference for how much copy belongs on each slide. The generic framework files say "≤3 lines" and "don't say in five words what you can say in one" — **that produces thin, generic carousel copy.** Override those defaults here.

## The problem to avoid

- One-sentence `P1` and one-sentence `P2` on every slide
- Slides that read like tweet threads, not carousel teaching
- Empty-looking text boxes in Canva (too much whitespace)
- Copy that sounds like a template, not Amir

## Amir on carousels

Amir is **direct**, not **sparse**. His emails and posts use:
- Short sentences — but **several of them per thought**
- Parenthetical asides and callbacks
- Transitions: "Here's the deal:", "But here's the thing:", "Listen…"
- A contrarian setup, then the unpack, then the punch

**Carousel body slides should feel like a tight paragraph from an email** — not a headline with two bullets.

## Per-field targets (body slides in use)

| Field | Target | Notes |
|-------|--------|-------|
| `Body{N}_Heading` | 5–12 words | Tip/takeaway label. Can be punchy. |
| `Body{N}_P1` | **35–70 words** | 2–4 sentences. Set up the idea. Context, reframe, or story beat. |
| `Body{N}_P2` | **25–55 words** | 2–3 sentences. Payoff, example, aside, or "perfect for" qualifier folded in. |

**Per body slide total:** aim for **60–120 words** across `P1` + `P2` when the slide is doing real work.

Unused body slides (`Body6`/`Body7` when the carousel only needs 5): single space ` ` in all three fields.

## Slide-type guidance

| Slide role | Density |
|------------|---------|
| **Early body (slides 2–3)** | Still substantive. "Light" means no wall of text — not one-liners. Hook + reframe in full sentences. |
| **Meat slides (4–7)** | Fullest copy. Examples, specifics, parenthetical color. |
| **Takeaway** | 15–35 words. One strong statement — can be 2 sentences if needed. |
| **CTA_Question** | 5–15 words |
| **CTA_Steps** | Both steps with brief context if needed |

## Voice patterns to weave in (when natural)

- Parenthetical aside in `P1` or `P2`
- Signature transition once per carousel minimum
- Contrarian beat → unpack → punch
- Occasional fragment for rhythm — **after** a developed thought, not instead of one

## Anti-patterns

| Don't | Do instead |
|-------|------------|
| `P1`: one sentence. `P2`: one sentence. | Develop the idea across both fields |
| Strip all personality to "fit" the slide | Split across `P1`/`P2` or add a body slide |
| Summarize the lesson in ≤10 words per field | Teach it — the swipe is cheap, the aha is not |
| Generic listicle tone | Amir's POV from `core-lessons.json` when relevant |

## Density check (before delivery)

For each body slide in use, ask:
1. Could I remove a sentence without losing meaning? If yes, **only remove one** — you're probably still too thin.
2. Does `P2` add a **new** beat (example, aside, qualifier) — not just restate `P1`?
3. Read aloud: does it sound like Amir talking, or a LinkedIn influencer's bullet list?

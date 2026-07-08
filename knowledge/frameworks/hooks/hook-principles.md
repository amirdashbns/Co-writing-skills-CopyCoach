# Hook Principles

Reference for Layer 1 of the content system: **angles and hooks** that stop the scroll, open emails, and carry across every platform.

Hooks are not headlines. A hook is a **proof + promise + curiosity** package that can be expressed as a subject line, IG slide, LinkedIn opener, blog title, or thread hook — same spine, different cut.

---

## What a hook must do

| Pillar | Job | Test |
|--------|-----|------|
| **Big promise** | Reader knows what they get if they keep reading | Can they picture the payoff? |
| **Curiosity** | Reader asks "what?" or "how?" | Is there an open question they need closed? |
| **Against the grain** | Challenges what the industry preaches | Does it contradict conventional advice with a specific result? |
| **Tangible results** | Concrete, realistic outcomes — not vague hype | "Open rates double while you spend half the time writing" beats "get more sales" |
| **Conversational register** | Reads like a viral social post, not a brochure | Would you say this out loud to a friend? |

**Proof + promise combo:** The reader must believe *you* (credibility) and want *the payoff* (benefit). Example: "I analyzed 1,000 emails from top copywriters" (proof) + "7 injections that make boring emails world-class" (promise).

**No arbitrary word limits.** Modern hooks are often one to three sentences. Compress per platform later — not at the idea stage.

---

## Six timeless principles (2025 twist)

From scroll-stop psychology. Apply to every hook type.

### 1. Poke at the pain — specifically
Don't say "most people struggle with X." Walk through the exact frustrating journey with vivid details.

- Weak: "Writing hooks is hard."
- Strong: "You chase the client for weeks… end up with a Word doc graveyard… and a pile of 'Will circle back soon' emails."

Turn empathy up. Harsh-truth guru vibes down.

### 2. Add credibility — specifically
Generic credentials are dead. Proof must feel like it could only come from someone who was there.

- Weak: "I've helped hundreds of businesses."
- Strong: "I pasted his own email into Claude, handed him his phone, and watched him forget to drink his Mai Tai."

### 3. Get specific with outcomes
Skeptical readers have been burned by "10x" promises. Use numbers that feel lived-in.

- Weak: "10x your engagement."
- Strong: "One prompt. His email. Ten seconds. He stopped mid-sip."

### 4. Leave a cliffhanger — sophisticated tension
Basic suspense is numb. Admit being wrong, validate conventional wisdom, then hint at the missing piece.

- Weak: "You won't believe what I discovered."
- Strong: "I thought educational posts were the whole game. They're not. But they're not the problem either."

### 5. Build intrigue — with clear value
Mystery without stakes is clickbait. Set up real business or human stakes, then stop at the key moment.

- Weak: "The surprising truth about LinkedIn growth:"
- Strong: "Prospect wanted negotiation training. We didn't sell it. Instead of pitching, I asked one question…"

### 6. Inspire — with the messy middle
Picture-perfect success stories are played out. Contrast recent win with early struggle.

- Weak: "Build a six-figure business working 4 hours a day."
- Strong: "Yesterday I made $34k in 5 days. My first product? $100 in 30."

---

## Six hook types (lenses)

Use as **generation lenses** — run the same topic through 1–2 types, pick the strongest.

| Type | What it does | When to use |
|------|--------------|-------------|
| **Pattern interrupt** | Defies prediction; cognitive dissonance | Contrarian POV, myth-bust, "everyone says X, I did Y" |
| **Problem validation** | Articulates their struggle better than they can | ICP pain from `icp.json`, editing death spiral, blank prompt box |
| **Curiosity gap / open loop** | Opens a question; delays payoff | Tease result before method; story with unfinished business |
| **Story & transformation** | Before/after arc with human detail | Case studies, personal bets, demo moments (phone handoff) |
| **Social proof & bandwagon** | Others like them got results | Client wins, "1,000 emails analyzed," crowd behavior |
| **Contrarian & polarizing** | Stakes a position against the industry | Core lessons that counter norms; willing to offend some |

Types can combine. "Copywriter friend said AI writes slop" = Story + Contrarian + Pattern interrupt.

---

## Psychology (why these work)

- **Dopamine / anticipation** — brain rewards expected insight, not just delivery. Hint specific value; don't overpromise.
- **Recognition response** — "that's exactly how I feel" beats clever wordplay. Mine `market-intelligence.json` and ICP language.
- **Curiosity gap** — gap must feel important, answerable, and non-obvious.
- **Pattern interrupt** — manufactured shock is tired; genuine insight still stops the scroll.

---

## Platform packaging (full brief standard)

One locked angle. Multiple surfaces. **Do not rewrite the angle per platform — adapt the cut.**

| Surface | Role |
|---------|------|
| `long_form` | Full conversational hook — no word cap. Source of truth. |
| `email_subject` | Curiosity + specificity; can use incongruent juxtaposition |
| `ig_slide_1` | Promise-forward; benefit + swipe motivation |
| `ig_slide_2` | Proof + bridge — **second-chance hook** when IG re-serves slide 2 |
| `linkedin_opener` | Can be longer; story-led or validation-led |
| `blog_title` | SEO + intrigue balance |
| `x_thread_hook` | Punchy; often contrarian or one-line curiosity |
| `threads_bluesky_hook` | Conversational; slightly more casual than LinkedIn |
| `reel_hook_spoken` | First 3 seconds; verbal pattern interrupt |
| `story_hook_text` | Ultra-short overlay text for IG Story |

See `angle-brief-schema.md` for the full handoff object passed to draft skills.

---

## Anti-patterns

| Avoid | Why |
|-------|-----|
| "Most people suck at X" | Played out; low empathy |
| Vague multipliers ("10x," "game-changer") | Skepticism trigger; check `never_say` in voice DNA |
| Clickbait without payoff | Burns trust; curiosity gap must be answerable |
| Hook with no proof anchor | "Magic wand" — who are you to say this? |
| Hook with no tangible promise | Curiosity alone isn't enough |
| Re-angling in draft skills | Slide 1/2 meaning locked at Layer 1 |

---

## Voice override

Framework patterns are **scaffolds only**. Every hook must pass through `/context/voice-dna.json` and sound like the user — not the template voice. Check `never_say` before delivery.

Anchor paradigm-shift hooks on ONE lesson from `/context/core-lessons.json` when relevant. See `idea-factory.md` for how stems connect to lessons.

---

## Subject line tactics (email)

When generating `email_subject` variants, optional lenses from the T.A.L.E. guide:

1. **Incongruent juxtaposition** — two contrasting ideas ("Disgraced Prada ambassador's dog barking cure")
2. **Specific visual benefit** — concrete outcome, not "peace" or "success"
3. **Punchy and concise** — cut filler ("how," "why," "can") when it doesn't earn its place
4. **Imply a specific solution** — "reveals," "unlocks," "holds key"
5. **Aligned with email voice** — subject tone matches body tone

Use 1–10 scales in edit passes for punchiness, curiosity, sensationalism — not during initial angle generation.

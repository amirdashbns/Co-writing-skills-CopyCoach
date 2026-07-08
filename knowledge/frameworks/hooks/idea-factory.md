# Idea Factory

Reference for generating **story stems** and **hook angles** by connecting real-world material to **core lessons**. Source: Email Mimic Prompts guide ("Infinite Ideas Factory") + system extensions.

**Core mechanic:** Creativity = making connections between patterns. You don't invent lessons each time — you connect daily observations, news, proof, and audience pain to lessons you already teach.

```
Core lesson (fixed spine)
    + Story stem (observation / news / case / controversy)
    = Hook angle → full angle brief (see angle-brief-schema.md)
```

---

## Before you prompt

1. **Core lessons must exist.** Read `/context/core-lessons.json`. One lesson per idea — never orphan content.
2. **Low-hanging fruit first.** Some stories are always available (see Evergreen stems). Use them before reaching for AI.
3. **Pay attention.** Coffee shop, client DM, industry headline, Reddit thread — stems are everywhere if you're looking.
4. **Be unpredictable but reliable.** Rotate categories. Keep telling stories. Readers should wonder what's next — not wonder where you went.

---

## The five original categories (MAHA / Amir guide)

### 1. Controversial opinion
Stake a position against the grain. If you don't have a unique POV, why are you in the market?

- What do you believe that experts in your niche get wrong?
- What stories or anecdotes prove your position?
- Example: Dog training — everyone teaches "be the alpha"; you teach gentle guidance.

**Pairs well with:** Contrarian hooks, core lessons that establish marketplace position.

### 2. Myth buster
What false beliefs keep your market stuck or prevent them from buying?

- What are they doing "right" that still isn't working?
- What outdated advice is hurting them?
- Example: Fitness — saturated fat myth; calorie surplus vs. single-ingredient blame.

**Pairs well with:** Problem validation, curiosity gap ("what should they believe instead?").

### 3. Pop culture reference
Song, TV, film, novel, meme — bonus if you know your audience loves it.

- Entrepreneur audience → Shark Tank, Michael Scott energy, etc.
- Use as **entry point**, not the whole lesson. Connect to core lesson fast.

**Pairs well with:** Pattern interrupt, conversational register.

### 4. News story reference
Tap conversations already in the reader's head. **Industry news often beats general news** — anxieties, platform changes, stupid moves by big players.

- General news: celebrity drama, cultural moment (use ethically; don't punch down).
- Industry news: algorithm change, tool update, guru meltdown, policy shift.
- Example: SEO teacher writes about whatever Google broke this week.

**Pairs well with:** Credibility, authority positioning, timely hooks.

**Quick tactic:** Grab a headline → link or paste → ask AI to connect to a core lesson and T.A.L.E. story. (Future: `market-hook-scanner` skill automates stem collection.)

### 5. Customer success / case study
Embedded proof as story. **Don't overuse** — sprinkle in.

Rules:
- Must embed a **specific lesson** — not "we're so great."
- Exceptional or interesting backstory wins.
- Example: Client went from 1,000 mass cold emails/month (5 clients) to dozens of personalized emails/week (5 clients/week). Lesson: personalization beats volume.

**Pairs well with:** Social proof, story & transformation hooks.

---

## Extended categories (system additions)

| # | Category | Stem source | Example |
|---|----------|-------------|---------|
| 6 | **Objection flip** | `icp.json` objections | "AI can't capture my voice" → demo story that demolishes it |
| 7 | **Before/after demo** | Your own tests | Same email, before/after Style Guide prompt |
| 8 | **Audience language harvest** | `market-intelligence.json`, Reddit | Hook built from exact quote: "45 min editing AI output" |
| 9 | **Tool / platform shock** | Product updates, policy | ChatGPT change, IG algorithm, new "prompt pack" drama |
| 10 | **Personal failure / old belief** | Your history | "I used to think educational posts were the whole game" |
| 11 | **DM / client question** | Real inbox | "Got asked this three times this week…" |
| 12 | **Competitor advice teardown** | Industry norms | "Everyone teaches 500 prompts. Here's why that's backwards." |
| 13 | **Micro-moment** | Daily life | Grocery store, coffee shop, airport, spanish latte — connect to lesson |
| 14 | **Specific data point** | Real numbers only | "Saves 3 hours every week" — never fake math |
| 15 | **Industry + pop culture mashup** | Both lenses | Michael Scott on a sales call → secondary rewards lesson |

---

## Evergreen stems (always available)

Use when nothing "exciting" happened today:

- Something you believed 2 years ago that was wrong
- A client question you answered this week
- A myth you still see taught in courses
- A tool you tried so they don't have to
- A before/after from your own workflow
- A contrarian take from `core-lessons.json`
- A phrase from ICP's internal monologue (`icp.json`)
- A Reddit pain point from latest market scan

---

## Connection workflow (manual)

**Step 1 — Capture the stem** (1–3 sentences)
> "Copywriter friend bet me AI only writes slop. I pasted his email into Claude with my Style Guide prompt. He froze mid-Mai-Tai."

**Step 2 — Score against core lessons**
Which 1–3 lessons does this naturally illustrate?

**Step 3 — Pick ONE lesson** (required)
Multi-lesson emails dilute. One paradigm shift per piece.

**Step 4 — Draft angle brief stub**
Proof anchor, promise, curiosity question, hook type, category tag.

**Step 5 — Expand to full brief**
All platform surfaces. Hand off to draft skills.

---

## Idea Factory prompt pattern

Use in the same conversation thread after voice/context is loaded (or in the hook-angle skill).

```
I want hook/story ideas for content based on one core lesson per piece.

Core lessons:
[PASTE FROM core-lessons.json OR LIST]

Story stem (something I witnessed / experienced / read today):
[1–3 SENTENCES]

Connect this stem to the best-fit core lesson(s).
Give me 3–5 ideas. For each:
- Which core lesson
- Idea factory category (controversial / myth_buster / pop_culture / news / case_study / etc.)
- One-sentence angle
- Proof anchor (why should they believe me)
- Tangible promise (what they get)
- Curiosity question it opens
- Suggested hook type(s)
```

For **cold generation** (no stem), add:
```
Also suggest 3 story stems I could pursue this week from evergreen sources and [ICP pain / market intelligence].
```

---

## Rotation guide

Don't hammer one category. Suggested mix over 10 pieces:

| Category | Target frequency |
|----------|------------------|
| Controversial / myth buster | 3–4 |
| Micro-moment / daily story | 2–3 |
| News / industry | 1–2 |
| Case study | 1–2 |
| Pop culture | 1 |
| Objection flip / demo | 1–2 |

Adjust for launches (more case study + offer connection) or audience fatigue (more micro-moment, less polarizing).

---

## Quality check (idea stage)

Before expanding to full angle brief:

- [ ] One core lesson — not zero, not three
- [ ] Stem is specific enough to picture (not abstract)
- [ ] Proof anchor exists or is obtainable
- [ ] Promise is tangible and realistic
- [ ] Curiosity gap is real — there's a question worth answering
- [ ] Not pure "value/how-to" — teaches what/why, sells how (presell logic)
- [ ] Could become email, carousel, LinkedIn, or thread without changing the angle

---

## Future: Market Hook Scanner

A sibling to `reddit-market-scanner` will output tagged stems:

```
knowledge/research/hook-stems-YYYY-MM-DD.json
```

Hook skill reads this file in **Factory mode** when present. Scanner collects; factory connects; hook skill packages the brief.

---
name: hook-angle
description: Generate hook angles and full platform briefs (proof + promise + curiosity) for any content type. Use when the user wants hooks, titles, angles, subject lines, story ideas, Idea Factory connections, or Layer 1 before writing email, carousel, LinkedIn, blog, or social content.
---

# Hook & Angle Generator (Layer 1)

Generate **angle briefs** — locked hooks that feed every downstream format (email, carousel, LinkedIn, blog, X, reel, story). This skill does **not** write full body copy. It produces the spine.

## Dependencies

Framework library at `/knowledge/frameworks/hooks/`:
- `hook-principles.md` — pillars, six principles, six hook types, psychology, anti-patterns
- `idea-factory.md` — story stems, 15 categories, connection workflow, rotation
- `angle-brief-schema.md` — output schema and handoff contract

Optional pattern library (if present):
- `/knowledge/frameworks/instagram-content/post-title-formulas.md` — fill-in title patterns

Context profiles:
- `/context/voice-dna.json` — voice filter (REQUIRED)
- `/context/icp.json` — pain, objections, language
- `/context/business-profile.json` — offers, positioning, CTAs
- `/context/core-lessons.json` — paradigm-shift spine (if present)
- `/context/market-intelligence.json` — audience language, pain quotes (if present)

Optional research input:
- `/knowledge/research/hook-stems-*.json` — future market-hook-scanner output
- Latest reddit scan in `/knowledge/research/`

## THE #1 RULE: Proof + Promise

Every angle must answer:
1. **Who are you to say this?** (`proof_anchor` — specific, vivid)
2. **What do I get?** (`tangible_promise` — concrete, realistic)
3. **What question am I left with?** (`curiosity_question`)

No magic wand. No arbitrary word limits on `long_form`. Compress per platform in the `hooks` block — not at the idea stage.

## Three modes (pick automatically or ask)

| Mode | Trigger | Input | Output |
|------|---------|-------|--------|
| **A — Generate** | "give me hooks", "ideas for…", blank page | Context profiles only | 3–5 angle brief stubs → expand chosen one to full brief |
| **B — Expand** | User brings rough hook, story dump, half-formed idea | Their words + context | 3–5 variations + full brief for pick; refine on feedback |
| **C — Factory** | "connect this to a lesson", daily observation, news link | Story stem + core lessons | 3–5 lesson-connected ideas → full brief for pick |

**Hybrid:** User gives topic + rough idea → run Factory connection first, then Expand variations on the best fit.

**Default when unsure:** Ask one question — "Do you have a story seed, or should I generate from your profile?"

---

## Before generating

1. Read `hook-principles.md` and `angle-brief-schema.md`
2. Read voice-dna, icp, business-profile (always)
3. Read core-lessons if present; if missing, extract 3–5 POV themes from voice + business context
4. Read market-intelligence if present
5. Check `/knowledge/research/hook-stems-*.json` for tagged stems (Factory mode)
6. If context profiles are placeholders, ask for niche + audience + offer

---

## Mode A — Generate (cold)

Use when user has no seed. **Expect lower hit rate** — offer more options.

### Phase A1 — Mine sources
Pull hook seeds from:
- Core lessons (one lesson per angle)
- ICP objections and `content_hooks` / internal monologue
- Market intelligence quotes and pain points
- Evergreen stems from `idea-factory.md`
- Business content pillars

### Phase A2 — Draft 5 angle stubs
For each stub (label A–E):
- `core_lesson_summary`
- `idea_factory_category`
- `story_stem` (proposed — may be hypothetical micro-moment; flag if needs real proof)
- `proof_anchor` / `tangible_promise` / `curiosity_question`
- `hook_types`
- `strength_notes`

### Phase A3 — User picks
Wait for selection unless user said "just pick the best."

### Phase A4 — Full brief
Expand chosen stub to complete `angle_brief` YAML per schema — all platform hooks.

---

## Mode B — Expand (rough idea)

Use when user provides story dump, hook draft, subject line attempt, or notes.

### Phase B1 — Extract spine
From their input, identify (or ask once if missing):
- Story stem
- Proof anchor
- Tangible promise
- Belief shift / core lesson fit

### Phase B2 — Generate variations
Produce **3–5 distinct angles** on the same material — not synonym swaps. Vary:
- Hook type lens (contrarian vs validation vs story)
- Proof emphasis vs promise emphasis
- IG slide 1 framing (benefit-first vs curiosity-first)

Present as labeled stubs with `strength_notes`.

### Phase B3 — Full brief
User picks (or combine: "slide 1 from B, opener from C") → output complete YAML.

### Phase B4 — Refine loop
On feedback ("more proof", "less guru", "punchier subjects"):
- Edit **wording only** — do not change locked meaning per handoff contract
- Regenerate affected `hooks` fields
- Use 1–10 scales if user says "more punchy" / "more curiosity"

---

## Mode C — Factory (stem → lesson)

Use when user has a observation, news item, case study, or market stem.

### Phase C1 — Lock the stem
1–3 sentences in their words. Do not over-polish.

### Phase C2 — Connect to lessons
Score against `core-lessons.json`. Return 3–5 connections:
- Lesson matched
- Category tag
- One-sentence angle
- Proof / promise / curiosity
- Hook types

Follow prompt pattern in `idea-factory.md`.

### Phase C3 — Pick + expand
User selects → full `angle_brief` YAML.

**News/industry:** Prefer industry news over general celebrity gossip unless user provides it.

---

## Full brief requirements

Every delivered `angle_brief` MUST include:

```yaml
angle_brief:
  version: "1.0"
  created_for_topic: ""
  core_lesson_id: null
  core_lesson_summary: ""
  belief_shift: ""
  idea_factory_category: ""
  story_stem: ""
  proof_anchor: ""
  tangible_promise: ""
  curiosity_question: ""
  hook_types: []
  hooks:
    long_form: ""
    email_subject: []      # 3–5 variants
    ig_slide_1: ""
    ig_slide_2: ""         # proof + bridge — second-chance hook
    linkedin_opener: ""
    blog_title: ""
    substack_title: ""
    x_thread_hook: ""
    threads_bluesky_hook: ""
    reel_hook_spoken: ""
    story_hook_text: ""
  offer_connection: ""
  repurposing_notes: ""
  suggested_format: ""
  angle_label: ""
  strength_notes: ""
```

**Write `long_form` first.** Derive all platform cuts from it.

### Platform rules (summary)
- `ig_slide_1` — promise-forward; benefit + swipe motivation
- `ig_slide_2` — proof + bridge; assume IG re-served this slide
- `email_subject` — specific > clever; incongruent juxtaposition OK
- `reel_hook_spoken` — first 3 seconds; verbal pattern interrupt

---

## Save output (when useful)

Save full brief to:
`knowledge/drafts/angle-brief-{topic-slug}.yaml`

Tell user the path. Downstream skills read this file when continuing.

---

## Output format (every run)

1. **Mode used** + one-line why
2. **Angle stubs** (if multiple) — table or labeled list for selection
3. **Full angle brief** — YAML block for chosen angle
4. **Next step** — one line: "Brief locked → run [email/carousel/linkedin] skill with this brief"

Do **not** write email body, carousel slides, or LinkedIn post here.

---

## Quality checklist

- [ ] Proof anchor is specific (not "I'm an expert")
- [ ] Promise is tangible (not "more engagement")
- [ ] Curiosity question is real — reader would want an answer
- [ ] One core lesson per angle
- [ ] `ig_slide_1` ≠ `ig_slide_2` (promise vs proof)
- [ ] Voice DNA applied; no `never_say` phrases
- [ ] Anti-patterns avoided (`hook-principles.md`)
- [ ] Full platform brief populated
- [ ] Handoff contract respected — meaning locked for draft skills

---

## Downstream handoff

Pass the YAML to:
- Email writer (T.A.L.E. body) — not built yet; use general voice + brief
- `instagram-carousel` skill — slides inherit `ig_slide_1`, `ig_slide_2`, `belief_shift`
- `linkedin-post`, `twitter-thread`, `substack-note`, `thought-leadership`

Draft skills **must not** re-angle. Edit skills **may** tighten words only.

---

## Notes

- Mode A runs dry without fresh stems — rotate Factory + market research
- User story dumps = Mode B, not Mode A
- When user pastes almost-full email like the copywriter friend story, extract spine and offer variations — don't rewrite the whole piece unless asked
- Future `market-hook-scanner` feeds Mode C with pre-tagged stems

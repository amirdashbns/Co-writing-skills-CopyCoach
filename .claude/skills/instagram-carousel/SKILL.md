---
name: instagram-carousel
description: Write binge-worthy Instagram carousels (slides + caption) that match the user's voice, target their audience, and drive engagement. Use when the user wants an Instagram carousel, IG post, carousel slides, or to repurpose content into a carousel.
---

# Instagram Carousel Writer

Write high-performing Instagram carousels — slide-by-slide copy plus a matching caption — using proven frameworks, filled in the user's authentic voice.

## Dependencies

This skill reads from a shared framework library at `/knowledge/frameworks/instagram-content/`:
- `content-buckets.md` — the 4 buckets + sub-buckets (the taxonomy)
- `brainstorm-questions.md` — idea-generation prompts by bucket
- `post-title-formulas.md` — Slide 1 title patterns
- `carousel-formulas.md` — the 16 slide-by-slide formulas
- `caption-templates.md` — caption structures by bucket
- `plug-and-play-ctas.md` — CTA library
- `power-word-bank.md` — power words/phrases by emotion
- `canva-template-setup.md` — Canva Bulk Create field names, column order, and workflow

And the context profiles in `/context/` (including `core-lessons.json` — the user's unique POVs). If you ever relocate this skill, move or re-point the framework library with it.

## THE #1 RULE: Voice Override

The frameworks provide **structure and persuasion logic only**. Every word you write must be in the **user's voice** from `/context/voice-dna.json` — never the framework's voice. The reference files are written in a generic/casual template voice; do not copy their phrasing, slang, or emoji style. Use their *skeleton*, the user's *flesh*.

Before finalizing, check the user's `never_say` list and tone profile. If a power word or template phrase violates it, cut it.

## Before Writing

1. **Read context profiles:**
   - `/context/voice-dna.json` — match the user's voice (REQUIRED)
   - `/context/icp.json` — write for the target audience, use their language
   - `/context/business-profile.json` — reference offers and CTAs accurately
   - `/context/market-intelligence.json` — ground pain points and language in real data (if present)
   - `/context/core-lessons.json` — the user's unique POVs / paradigm shifts (if present); anchor paradigm-shift posts on one of these
2. **Check `/knowledge/` for source material** if repurposing an existing piece (article, newsletter, transcript).

## Workflow

### Phase 1 — Pick the bucket + sub-bucket
Read `content-buckets.md`. Based on the user's topic and goal, recommend the best-fit **bucket** (Educate / Relate / Inspire / Sell) and **sub-bucket** (e.g. Problem Awareness, Case Study, Self-Selection). Explain why in one line, and confirm with the user (or proceed with the obvious choice if the topic makes it clear). Default mix skews Educate/Relate unless the user is actively selling/launching.

### Phase 2 — Lock the idea (and anchor on a core lesson when relevant)
A carousel is only as good as its idea. Use the matching prompts in `brainstorm-questions.md` to pin down **one specific audience problem** the carousel solves, meeting the audience at their:
- day-to-day struggle (from `icp.json`)
- experience level (don't teach advanced theory to beginners)
- knowledge of the user's offers (don't assume they know the offer — give context)

**Anchor on a core lesson WHEN RELEVANT.** If the post is a paradigm-shift type — Problem Awareness, Turning Point, Value Share, Self-Selection, or FAObjection — pick ONE lesson from `/context/core-lessons.json` to be the post's central "aha." This is what makes the content unmistakably the user's POV, not generic advice. Use the lesson's `the_aha` and `deeper_truth` as the spine, its `one_liners` as hook material, and `audience_belief_it_shifts` to frame the problem. Teach the "what" and "why" of the lesson; let the CTA point to the "how" (the offer).

**Skip the core lesson** for pure plug-and-play lists, behind-the-scenes, or engagement-invitation posts — not everything is a paradigm shift, and forcing one makes it feel preachy. Use judgment.

Confirm the single, specific topic (and the core lesson, if used) before writing. Get specific: not "everything about X" but one focused slice (e.g. not "how to use every gym machine" but "how to set up a barbell for hip thrusts").

### Phase 3 — Write Slide 1 (clickable post title)
Use `post-title-formulas.md` (start with the chosen bucket's section, but borrow freely). Rules:
- 5-7 words ideal, under 10 always
- Clear enough that a feed-scanner instantly gets the topic
- Pique interest: challenge a belief, surprising stat, reveal a truth, or story hook
- Layer in a power word if it fits the voice (`power-word-bank.md`)
- Offer 2-3 title options for the user to choose from

### Phase 4 — Write Slides 2-9 (the body)
Pick the matching formula from `carousel-formulas.md` (each is tagged "Perfect for: [sub-bucket]"). Follow its slide-by-slide structure. Apply the **3 pillars** throughout:
- **Value** — every slide useful for *this* audience
- **Momentum** — each slide leads to the next; first 3 slides matter most; use seeds of curiosity, direct words, or arrows. Keep slides 1-3 light (heading + short subheading), don't overwhelm up front.
- **Readability** — headings (tips/takeaways, not titles) + subheadings (one-liners) + body (≤3 lines, ~3rd-grade reading level). Don't say in five words what you can say in one.

Follow the **hourglass flow**: zoomed-out big picture → zoom in (context/reframe) → get specific (the meat) → zoom back out (big takeaway) → connect to the user/offer.

### Phase 5 — Write Slide 10 (CTA)
Pick from `plug-and-play-ctas.md` matched to the goal (offer, lead, engagement). Connect it with a natural lead-in so it doesn't feel like a sales pitch. If the post relates to an offer in `business-profile.json`, give context on the offer (don't just name it). For video carousels, combine the CTA with the big-takeaway slide so it lands naturally.

### Phase 6 — Write the caption
Use `caption-templates.md` (match the same bucket; pick by the "to use when" purpose). The caption must **NOT repeat the slides** — expand on them, tell a story behind them, add a fresh angle, or at minimum say it differently. Hook first line, CTA last, 3-4 keyword mentions for caption SEO.

### Phase 7 — Add hashtags
- **Hashtags:** suggest 3-5, mixing popular + niche-specific based on the topic.

### Phase 8 — Emit Canva Sheet data
Read `canva-template-setup.md` for the field map, column order, and paste workflows. The **carousel copy (steps 1–6) is the source of truth**. Phase 8 maps that copy into fields — it does not rewrite or shorten it.

**Words over design:** Split across `P1` + `P2`, or add body slides — never cram or cut copy.

**25 fields** (no `PerfectIf`): `Title` → `Body1_Heading` … `Body7_P2` → `Takeaway` → `CTA_Question` → `CTA_Steps`. See `canva-template-setup.md` for mapping rules.

**Canva Sheets does NOT split tab paste.** A tab-separated line pasted into A2 lands entirely in one cell. Do not tell the user to paste TSV directly into Canva Sheets.

**Field value rules (critical):**
- **No tab characters inside field values.** No newlines inside field values. Use ` / ` to join CTA steps; use spaces in `Takeaway` instead of line breaks.
- Unused body slides (6–7): single space ` ` in each of that slide's three fields.
- If only one paragraph on a slide: all copy in `P1`, single space ` ` in `P2`.
- Never leave `P2` empty for a slide in use — Canva drops empty columns.

**Deliver all three of the following:**

#### 1. Labeled field blocks (always — foolproof)
One section per field, in exact column order (A→Y). Each section: field name, target cell, and a fenced copy block with **only** that field's value. Example:

```
### Title → A2
(paste into cell A2)
```

User pastes each value into the matching row-2 cell under the header.

#### 2. Row files (when writing to disk is possible)
Save to `knowledge/drafts/{topic-slug}-canva-row.tsv` and `{topic-slug}-canva-row.xlsx` (2 rows: headers + data). Use `scripts/build-canva-carousel-row.py` or write equivalent files. Tell the user:

- **Fastest in Canva:** Actions → Import data → upload the `.xlsx`
- **Google Sheets bridge:** open the `.tsv` in a text editor (tabs preserved), paste into Google Sheets A2, copy A2:Y2, paste into Canva Sheet A2

#### 3. Workflow reminder (one line)
Canva data loaded → open template → Bulk Create → Sheets → Carousel Data → Generate.

**Do not** output a single tab-separated code block as the primary paste method. Markdown code blocks strip tabs when copied from chat.

## Output Format

Deliver:
1. **Bucket + sub-bucket + formula used** (one line, with why) — and the **core lesson** anchoring the post, if one was used
2. **The carousel** — each slide numbered, labeled by purpose, with the copy
3. **2-3 alternative Slide 1 titles**
4. **The caption** (with hook + CTA)
5. **Canva Sheet data** — labeled field blocks + row files (see `canva-template-setup.md`)
6. **Hashtags** (3-5)

## Quality Checklist

Before delivering, verify:
- [ ] **Voice:** sounds unmistakably like `voice-dna.json`; no `never_say` words; not the framework's voice
- [ ] **POV:** if it's a paradigm-shift post, it's anchored on a core lesson (the "aha" is the user's, not generic)
- [ ] **Value:** solves one specific problem for the ICP at their experience level
- [ ] **Momentum:** Slide 1 grabs attention; first 3 slides pull the reader in; every slide earns the next swipe
- [ ] **Readability:** headings/subheadings/body hierarchy; short lines; no walls of text
- [ ] **Title:** clickable, under 10 words, clear topic
- [ ] **Caption:** does NOT repeat the slides; has a hook and a clear CTA
- [ ] **CTA:** specific, with a natural lead-in; offer context given if referenced
- [ ] ≤ 10 slides
- [ ] **Canva data:** 25 labeled field blocks in column order; row TSV+XLSX saved when possible; no tabs/newlines inside values; no empty `P2` on slides in use

## Notes
- Carousels suit Educate/Relate/Inspire/Sell content built around words. For highly visual/real-time content, a reel may fit better — but every formula here also works as a reel script outline.
- Generate related-content ideas (the next step and previous step a reader might take) so the user can build a bingeable feed.

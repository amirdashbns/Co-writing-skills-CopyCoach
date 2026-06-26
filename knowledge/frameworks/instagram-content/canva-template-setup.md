# Canva Carousel Template — Setup & Field Map

Reference for the **cream theme** 10-slide Instagram carousel template used with Canva Bulk Create.

## Philosophy: words over design

**Copy is the product. Design is the container.**

The carousel skill writes the full message first — voice, momentum, depth. The Canva table is an *export layer* that maps that copy into template fields. Never shorten or gut copy to fit a text box.

When copy and layout conflict:
1. **Split** across `P1` + `P2`, or add another body slide — don't cut
2. **Resize the template** to fit the writing (see Word-first template guide below)
3. Char guides below are **soft references for the stock template**, not rules for the writer

Default bias: **more words, more slides** — not tighter fields.

## Template structure (10 slides)

| Slide # | Role | Source layout | Notes |
|--------:|------|---------------|-------|
| 1 | Title | Page 2 (cream) | Swipe hook — split across 4 fields |
| 2–8 | Body | Pages 16–18 layout | Up to 7 body slides; leave unused slots blank |
| 9 | Takeaway | Page 6 (cream) | Big punchy statement — penultimate slide |
| 10 | CTA | Page 7 (cream) | Save + comment — final slide |

**Flexible length:** Fill only the body slides you need. After Bulk Create generates pages, delete any blank body slides before exporting.

## Field names (must match exactly)

When connecting data in Canva, each text box must use these field names. The skill outputs a table/CSV with these exact column headers.

### Slide 1 — Title

| Field | Purpose | Soft ref (stock template) |
|-------|---------|---------------------------|
| `Title_Line1` | Opening phrase | ~15 |
| `Title_Highlight` | Pink-pill emphasis | ~12 |
| `Title_Line2` | Middle line | ~15 |
| `Title_Line3` | Closing line | ~15 |

**Splitting the title:** Pick the most clickable word/phrase for `Title_Highlight` — a number, timeframe, or power word. Example: *"Stop Wasting Hours on Generic AI Posts"* → Line1: `Stop Wasting`, Highlight: `Hours`, Line2: `on Generic AI`, Line3: `Posts`.

### Body slides 2–8 — `Body1_` through `Body7_`

Each body slide uses four fields:

| Field | Purpose | Soft ref (stock template) |
|-------|---------|---------------------------|
| `Body{N}_Heading` | Slide heading (serif display) | ~60 |
| `Body{N}_P1` | First body paragraph | ~120 |
| `Body{N}_P2` | Second paragraph (optional) | ~120 |
| `Body{N}_PerfectIf` | Yellow callout after "Perfect if:" | ~80 |

**Mapping carousel copy to body fields:**
- Formula "heading" → `Body{N}_Heading`
- Formula "subheading" or first body block → `Body{N}_P1`
- Second body block (if any) → `Body{N}_P2`
- "Perfect for" / audience qualifier → `Body{N}_PerfectIf`

Keep early body slides lighter for momentum. Use `P2` and extra body slides when the idea needs room — that's the word-first default.

### Slide 9 — Takeaway

| Field | Purpose | Soft ref (stock template) |
|-------|---------|---------------------------|
| `Takeaway_L1` | First line (black) | ~20 |
| `Takeaway_Accent` | Pink emphasis word(s) | ~15 |
| `Takeaway_L2` | Next line(s) | ~25 |
| `Takeaway_L3` | Final line (optional) | ~25 |

`@YOURHANDLEHERE` stays static in the template — do not include in the data table.

### Slide 10 — CTA

| Field | Purpose | Char guide |
|-------|---------|------------|
| `CTA_Question` | Top question | ≤ 30 |
| `CTA_Step1` | First instruction | ≤ 25 |
| `CTA_Step2_Prefix` | Text before the keyword | ≤ 20 |
| `CTA_Keyword` | Pink highlighted comment keyword | ≤ 15 |
| `CTA_Step2_Suffix` | Text after the keyword | ~60 |

Example: `2) COMMENT '` + `VOICE` + `' TO GET MY FREE AI VOICE GUIDE`

The product mockup at the bottom of the CTA slide is decorative — swap the image manually in Canva if promoting a different lead magnet.

## Word-first template guide (when you lengthen slides)

The stock cream layouts were built for short demo copy. For a **word-first** template, resize once and save — the skill won't hold back.

**Body slides (pages 16–18 layout):**
- Drag text boxes **taller** — aim for 4–6 lines of body copy per `P1` / `P2`
- Drop body font to ~22–26pt (readable, not billboard)
- Keep heading display font but allow 2–3 lines of wrap
- Push the yellow PerfectIf box **lower** on the slide — give body text the top 60% of the canvas
- Use the page 18 layout (heading + 2 paragraphs) as your default body master

**Title slide:**
- Allow 2 lines per title field if needed — widen boxes to full content width

**Takeaway + CTA:**
- These stay punchy by nature — less room needed than body slides

**Sizing test:** paste your *longest real carousel* into connected fields. If anything overlaps, enlarge boxes — don't cut copy.

**Canva limitation:** Bulk Create does not auto-shrink font. The template must be sized for your voice, not the other way around.

## Bulk Create workflow

```
1. Run instagram-carousel skill  →  get slide copy + Canva data table
2. Open your 10-slide Canva template
3. Apps → Bulk Create (or Data Autofill)
4. Paste the table / upload CSV
5. Connect fields (first time only — names must match this doc)
6. Generate pages
7. Delete any unused blank body slides
8. Swap CTA mockup image if needed
9. Export as PNG or PDF for Instagram
```

## Full column order (for CSV)

Use this exact header row — 41 columns total:

```
Title_Line1,Title_Highlight,Title_Line2,Title_Line3,Body1_Heading,Body1_P1,Body1_P2,Body1_PerfectIf,Body2_Heading,Body2_P1,Body2_P2,Body2_PerfectIf,Body3_Heading,Body3_P1,Body3_P2,Body3_PerfectIf,Body4_Heading,Body4_P1,Body4_P2,Body4_PerfectIf,Body5_Heading,Body5_P1,Body5_P2,Body5_PerfectIf,Body6_Heading,Body6_P1,Body6_P2,Body6_PerfectIf,Body7_Heading,Body7_P1,Body7_P2,Body7_PerfectIf,Takeaway_L1,Takeaway_Accent,Takeaway_L2,Takeaway_L3,CTA_Question,CTA_Step1,CTA_Step2_Prefix,CTA_Keyword,CTA_Step2_Suffix
```

## Installable for clients

This file travels with `/knowledge/frameworks/instagram-content/`. To onboard a client:

1. Duplicate the Canva template in their account
2. Connect the same field names (or share a pre-connected template link)
3. Point their agent at this field map
4. They paste skill output into Bulk Create — no redesign needed

## Future: Autofill API (Enterprise)

The same field names map 1:1 to Canva Connect API autofill keys. If you upgrade to Canva Enterprise, only the delivery step changes (API instead of paste) — the skill output schema stays identical.

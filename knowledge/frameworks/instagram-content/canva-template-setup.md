# Canva Carousel Template — Setup & Field Map

Reference for the **cream theme** 10-slide Instagram carousel template used with Canva Bulk Create.

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

| Field | Purpose | Char guide |
|-------|---------|------------|
| `Title_Line1` | Opening phrase | ≤ 12 |
| `Title_Highlight` | Pink-pill emphasis (number, power word, or hook word) | ≤ 10 |
| `Title_Line2` | Middle line | ≤ 12 |
| `Title_Line3` | Closing line | ≤ 12 |

**Splitting the title:** Pick the most clickable word/phrase for `Title_Highlight` — a number, timeframe, or power word. Example: *"Stop Wasting Hours on Generic AI Posts"* → Line1: `Stop Wasting`, Highlight: `Hours`, Line2: `on Generic AI`, Line3: `Posts`.

### Body slides 2–8 — `Body1_` through `Body7_`

Each body slide uses four fields:

| Field | Purpose | Char guide |
|-------|---------|------------|
| `Body{N}_Heading` | Slide heading (serif display) | ≤ 45 |
| `Body{N}_P1` | First body paragraph | ≤ 70 |
| `Body{N}_P2` | Second paragraph (optional — leave blank if not needed) | ≤ 70 |
| `Body{N}_PerfectIf` | Yellow callout text **after** "Perfect if:" (label stays in template) | ≤ 55 |

**Mapping carousel copy to body fields:**
- Formula "heading" → `Body{N}_Heading`
- Formula "subheading" or first body block → `Body{N}_P1`
- Second body block (if any) → `Body{N}_P2`
- "Perfect for" / audience qualifier → `Body{N}_PerfectIf`

Keep early body slides light (short heading + one line). Use `P2` on meatier middle slides.

### Slide 9 — Takeaway

| Field | Purpose | Char guide |
|-------|---------|------------|
| `Takeaway_L1` | First line (black) | ≤ 15 |
| `Takeaway_Accent` | Pink emphasis word(s) | ≤ 12 |
| `Takeaway_L2` | Next line(s) | ≤ 18 |
| `Takeaway_L3` | Final line (optional) | ≤ 18 |

`@YOURHANDLEHERE` stays static in the template — do not include in the data table.

### Slide 10 — CTA

| Field | Purpose | Char guide |
|-------|---------|------------|
| `CTA_Question` | Top question | ≤ 30 |
| `CTA_Step1` | First instruction | ≤ 25 |
| `CTA_Step2_Prefix` | Text before the keyword | ≤ 20 |
| `CTA_Keyword` | Pink highlighted comment keyword | ≤ 15 |
| `CTA_Step2_Suffix` | Text after the keyword | ≤ 45 |

Example: `2) COMMENT '` + `VOICE` + `' TO GET MY FREE AI VOICE GUIDE`

The product mockup at the bottom of the CTA slide is decorative — swap the image manually in Canva if promoting a different lead magnet.

## Text overflow — fix in the template (one-time)

Canva Bulk Create **does not auto-shrink font size**. If copy is longer than the placeholder text, boxes overlap.

**Size your template using MAX-length dummy text**, not the short stock phrases from the pack. Paste these into each connected box, then resize boxes / reduce font until nothing overlaps:

| Field type | Max-length test string |
|------------|-------------------------|
| Title lines | `Stop Wasting` / `Hours` / `on Generic` / `AI Posts` |
| Body heading | `Why your ChatGPT prompts still sound generic` |
| Body P1 / P2 | `Paste your real writing first. Then ask for the new thing. Context beats instructions every time.` |
| PerfectIf | `You have been tweaking prompts for months and still sound robotic` |
| Takeaway lines | `STOP COLLECTING` / `PROMPTS.` / `START FEEDING IT` / `YOUR WRITING.` |
| CTA suffix | `' TO GET MY FREE AI VOICE GUIDE` |

**In Canva after connecting fields:**
1. Click each text box → drag the side handles to make boxes **taller/wider**
2. Select all body text → drop font size slightly (e.g. 28 → 24)
3. Text menu → **Advanced** → set **Anchor** so boxes grow downward, not into each other
4. Ungroup any grouped text+shapes before connecting data
5. Generate a test row → fix overflow once → save as template

**In the skill:** write shorter than the char guides above. If a thought is too long, split it across `P1` + `P2` or use two body slides — never overflow one field.

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

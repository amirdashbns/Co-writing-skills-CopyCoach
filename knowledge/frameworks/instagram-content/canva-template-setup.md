# Canva Carousel Template — Setup & Field Map

Reference for the **cream theme** 10-slide Instagram carousel template used with Canva Bulk Create.

## Philosophy: words over design

**Copy is the product. Design is the container.**

The carousel skill writes the full message first — voice, momentum, depth. The Canva table is an *export layer* that maps that copy into template fields. Never shorten or gut copy to fit a text box.

When copy and layout conflict:
1. **Split** across `P1` + `P2`, or add another body slide — don't cut
2. **Resize the template** to fit the writing (see Word-first template guide below)
3. Soft refs below are for the stock template, not rules for the writer

Default bias: **more words, more slides** — not tighter fields.

## Fewer fields, less legwork

**Don't split fields to match pink accents or line breaks.** That was over-engineered — more boxes = more overlap risk and more resizing after every generate.

| Slide | Fields | Why |
|-------|--------|-----|
| Title | **1** — `Title` | Full hook in one box. Pink pill highlight stays **static in the template** (or tweak manually after generate). |
| Body ×7 | **4 each** — `Heading`, `P1`, `P2`, `PerfectIf` | Heading + up to 2 paragraphs + yellow callout. That's the right granularity. |
| Takeaway | **1** — `Takeaway` | Full statement in one box. No per-line fields. |
| CTA | **2** — `CTA_Question`, `CTA_Steps` | Question on top; both instructions in one block below. |

**32 fields total** (not 41). Fewer connections, fewer things to overlap.

## Template structure (10 slides)

| Slide # | Role | Fields |
|--------:|------|--------|
| 1 | Title | `Title` |
| 2–8 | Body | `Body{N}_Heading`, `Body{N}_P1`, `Body{N}_P2`, `Body{N}_PerfectIf` |
| 9 | Takeaway | `Takeaway` |
| 10 | CTA | `CTA_Question`, `CTA_Steps` |

**Flexible length:** Fill only the body slides you need. Delete blank body slides after generate.

## Field names (must match exactly)

### Slide 1 — Title

| Field | Purpose |
|-------|---------|
| `Title` | Entire swipe-hook title. One text box. Line breaks OK inside the field if you want stacked lines. |

**In Canva:** Merge the old multi-line title boxes into **one** text box → connect to `Title`. Remove or keep the pink pill as a **fixed design element** (not data-driven).

### Body slides 2–8 — `Body1_` through `Body7_`

| Field | Purpose |
|-------|---------|
| `Body{N}_Heading` | Slide heading |
| `Body{N}_P1` | First body paragraph (can be multiple sentences) |
| `Body{N}_P2` | Second paragraph block (para 2+3 merged from template) |
| `Body{N}_PerfectIf` | Yellow callout text **after** "Perfect if:" (label stays in template) |

**Mapping:** heading → `Heading`; main copy → `P1`; extra paragraph → `P2`; audience qualifier → `PerfectIf`. Do **not** split every sentence into its own field.

### ⚠️ Canva drops empty columns

**Bulk Create will NOT show a column if the data cell is empty** — no `Body1_P2` in the field list, nothing to connect, nothing populates.

**Rules:**
- If a body slide is **in use**, every connected field (`P1`, `P2`, `PerfectIf`) needs **some text** in the spreadsheet row.
- If you only have one paragraph: put it all in `P1` and put a **single space** ` ` in `P2` (keeps the column visible; renders nearly invisible). Or merge into one box and don't connect `P2`.
- Unused body slides (6–7): leave empty and **delete those slides** after generate — or fill with `—` placeholders if you need the columns to appear during setup.

**Test file with all P2 filled:** `sample-canva-strategy-test.xlsx` (matches the 7-step template).

### Slide 9 — Takeaway

| Field | Purpose |
|-------|---------|
| `Takeaway` | Full punchy closing statement — all lines in one field |

**In Canva:** Merge `DO THIS FOR` / `4 WEEKS` / etc. into **one** text box → connect to `Takeaway`. Pink accent word is static in the template or you highlight after generate.

`@YOURHANDLEHERE` stays static — not in the data table.

### Slide 10 — CTA

| Field | Purpose |
|-------|---------|
| `CTA_Question` | e.g. `Found this helpful?` |
| `CTA_Steps` | Both instructions in one block, e.g. `1) SAVE FOR LATER` + line break + `2) COMMENT 'VOICE' TO GET MY FREE AI VOICE GUIDE` |

**In Canva:** Merge step 1 + step 2 text boxes into one → `CTA_Steps`. Pink keyword highlight stays static or edit after generate. Mockup image at bottom stays static.

## Reconnecting your template (one-time)

If you already connected the old 41-field layout:

1. **Title slide** — delete extra text boxes; one box for all title copy → `Title`
2. **Body slides** — keep 4 boxes each (heading, P1, P2, PerfectIf) — already correct
3. **Takeaway** — merge all statement text into one box → `Takeaway`
4. **CTA** — two boxes: question + combined steps → `CTA_Question`, `CTA_Steps`
5. Save template

## Word-first template guide (when you lengthen slides)

- Body boxes: taller, 4–6 lines per `P1` / `P2`, font ~22–26pt
- Push yellow PerfectIf lower — body gets top 60% of slide
- Takeaway + CTA: one tall box each is enough
- Size against your longest real carousel — enlarge boxes, don't cut copy

**Canva limitation:** Bulk Create does not auto-shrink font. Template serves copy.

## Bulk Create workflow

```
1. Run instagram-carousel skill  →  get slide copy + Canva data table
2. Open your 10-slide Canva template
3. Apps → Bulk Create → enter data manually / Google Sheets / upload CSV
4. Connect fields (first time only — 32 fields, names must match this doc)
5. Generate pages
6. Delete unused blank body slides
7. Export
```

## Full column order (for CSV)

**32 columns:**

```
Title,Body1_Heading,Body1_P1,Body1_P2,Body1_PerfectIf,Body2_Heading,Body2_P1,Body2_P2,Body2_PerfectIf,Body3_Heading,Body3_P1,Body3_P2,Body3_PerfectIf,Body4_Heading,Body4_P1,Body4_P2,Body4_PerfectIf,Body5_Heading,Body5_P1,Body5_P2,Body5_PerfectIf,Body6_Heading,Body6_P1,Body6_P2,Body6_PerfectIf,Body7_Heading,Body7_P1,Body7_P2,Body7_PerfectIf,Takeaway,CTA_Question,CTA_Steps
```

## Installable for clients

Duplicate the reconnected template + this field map. Paste skill CSV → generate.

## Future: Autofill API (Enterprise)

Same 32 field names map 1:1 to autofill keys if you upgrade later.

# Canva Carousel Template — Setup & Field Map

Reference for the **cream theme** 10-slide Instagram carousel template used with Canva Bulk Create + **Canva Sheets**.

## Philosophy: words over design

Copy is the product. The Canva Sheet row is an export layer. Never shorten copy to fit a text box.

## Field map — 25 fields

| Slide | Fields |
|-------|--------|
| Title | `Title` |
| Body ×7 | `Body{N}_Heading`, `Body{N}_P1`, `Body{N}_P2` |
| Takeaway | `Takeaway` |
| CTA | `CTA_Question`, `CTA_Steps` |

No `PerfectIf` — delete yellow boxes from template (or leave static).

## Two stages

| Stage | What | Text matters? |
|-------|------|----------------|
| **1. Setup (once)** | Row 1 = headers. Connect template boxes to fields. | Row 2 can be `test` / lorem ipsum — only headers + connections matter |
| **2. Produce (each carousel)** | Load new copy into row 2 → Generate | Yes — this is the real copy |

## Column order (left → right, 25 columns)

```
Title
Body1_Heading, Body1_P1, Body1_P2
Body2_Heading, Body2_P1, Body2_P2
Body3_Heading, Body3_P1, Body3_P2
Body4_Heading, Body4_P1, Body4_P2
Body5_Heading, Body5_P1, Body5_P2
Body6_Heading, Body6_P1, Body6_P2
Body7_Heading, Body7_P1, Body7_P2
Takeaway
CTA_Question
CTA_Steps
```

## ⚠️ Canva Sheets does NOT split tab paste

**Do not paste a tab-separated line directly into Canva Sheets.** Everything lands in cell A1 as one blob. Canva Sheets also has no “split text to columns” tool.

Copying from a chat/code block often **strips tab characters** (turns them into spaces), which makes the problem worse.

Use one of the workflows below instead.

---

## Workflow A — XLSX import (fastest in Canva)

Best when the agent saves row files for you, or you build them with `scripts/build-canva-carousel-row.py`.

1. Open **Carousel Data** Canva Sheet
2. **Actions → Import data** → upload the 2-row `.xlsx` (row 1 = headers, row 2 = copy)
3. Open template → **Bulk Create** → **Sheets** → pick Carousel Data → **Generate**

Re-import overwrites the data range — that is expected. Headers + field connections stay on the template.

---

## Workflow B — Google Sheets bridge (one clipboard paste)

Use when you have a `.tsv` row file (tabs preserved) or copied from a real text editor — **not** from a markdown code block.

1. Open any **Google Sheet**
2. Click cell **A2**, paste the tab-separated line → Google splits it into 25 columns
3. Select **A2:Y2**, copy
4. Open **Carousel Data** Canva Sheet, click **A2**, paste → columns should carry over
5. Bulk Create → Sheets → Generate

---

## Workflow C — Labeled fields (no extra tools)

The agent outputs one copy block per field, in column order. Paste each value into row 2 under its header:

| Col | Field | Paste into |
|-----|-------|------------|
| A | Title | A2 |
| B | Body1_Heading | B2 |
| C | Body1_P1 | C2 |
| … | … | … |
| Y | CTA_Steps | Y2 |

Slowest, but works everywhere. Use when import and Google Sheets are not an option.

---

## Field value rules

- No tab characters inside a field value
- No newlines inside a field value (use spaces in `Takeaway`; join CTA steps with ` / `)
- Unused body slides (6–7): single space ` ` in each of that slide's three fields
- Single-paragraph slide: all copy in `P1`, single space ` ` in `P2`
- Never leave `P2` empty for a slide in use — Canva drops empty columns

## One-time setup

### Row 1 headers

Import `carousel-data-headers.tsv` via **Actions → Import data**, or paste headers using Workflow B (Google Sheets bridge). Header line is in `carousel-data-headers.tsv`.

### Row 2 placeholder (setup only)

Any placeholder text across 25 cells while connecting template fields. Real copy only matters at produce time.

## Canva drops empty columns

Every connected column needs a value in row 2 (use ` ` if unused).

## Workflow summary

```
SETUP (once):  Headers in row 1 → connect template → save
EACH CAROUSEL: Import XLSX OR Google Sheets bridge OR paste field-by-field → Bulk Create → Generate → export
```

## Template tweaks

- Delete yellow PerfectIf boxes
- Merge title / takeaway / CTA into single boxes per field map
- Size P1/P2 boxes for word-first copy

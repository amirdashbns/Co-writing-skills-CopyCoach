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
| **2. Produce (each carousel)** | Paste new copy into row 2 → Generate | Yes — this is the real copy |

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

## Paste row format (no CSV files)

The agent outputs **one tab-separated line** — not comma-separated text, not a file download.

**Why tabs?** Pasting comma-separated text into a sheet puts everything in **one cell**. Tabs split into columns automatically.

**Each new carousel:**
1. Open **Carousel Data** Canva Sheet
2. Click cell **A2**
3. Paste the agent's tab-separated line
4. Open template → **Bulk Create** → **Sheets** → pick Carousel Data → **Generate**

**TSV rules:**
- One line, 25 fields, separated by **tab** characters
- No tabs or newlines inside a field value
- CTA steps: join with ` / ` (e.g. `1) SAVE FOR LATER / 2) COMMENT 'VOICE' FOR FREE GUIDE`)
- Unused body slides: space ` ` in each of that slide's three fields
- Single-paragraph slide: copy in `P1`, space ` ` in `P2`

## One-time setup

### Row 1 headers (paste into A1 once)

Tab-separated header line — copy from `carousel-data-headers.tsv` or paste:

```
Title	Body1_Heading	Body1_P1	Body1_P2	Body2_Heading	Body2_P1	Body2_P2	Body3_Heading	Body3_P1	Body3_P2	Body4_Heading	Body4_P1	Body4_P2	Body5_Heading	Body5_P1	Body5_P2	Body6_Heading	Body6_P1	Body6_P2	Body7_Heading	Body7_P1	Body7_P2	Takeaway	CTA_Question	CTA_Steps
```

### Row 2 placeholder (setup only)

Paste `test` tab `test` tab … across 25 cells, connect template fields, save.

## Canva drops empty columns

Every connected column needs a value in row 2 (use ` ` if unused).

## Workflow summary

```
SETUP (once):  Headers in row 1 → connect template → save
EACH CAROUSEL: Agent paste row → A2 → Bulk Create → Sheets → Generate → export
```

## Template tweaks

- Delete yellow PerfectIf boxes
- Merge title / takeaway / CTA into single boxes per field map
- Size P1/P2 boxes for word-first copy

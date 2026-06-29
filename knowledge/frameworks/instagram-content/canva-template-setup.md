# Canva Carousel Template — Setup & Field Map

Reference for the **cream theme** 10-slide Instagram carousel template used with Canva Bulk Create.

## Philosophy: words over design

**Copy is the product. Design is the container.**

The carousel skill writes the full message first. The Canva table is an *export layer*. Never shorten copy to fit a text box.

## Field map — 25 fields

| Slide | Fields |
|-------|--------|
| Title | `Title` |
| Body ×7 | `Body{N}_Heading`, `Body{N}_P1`, `Body{N}_P2` |
| Takeaway | `Takeaway` |
| CTA | `CTA_Question`, `CTA_Steps` |

**No `PerfectIf` fields** — delete the yellow boxes from the template (or leave static/empty). Audience qualifiers go in `P2` or an extra sentence in `P1`.

## Template structure (10 slides)

| Slide # | Role | Connect |
|--------:|------|---------|
| 1 | Title | `Title` |
| 2–8 | Body | `Body{N}_Heading`, `Body{N}_P1`, `Body{N}_P2` |
| 9 | Takeaway | `Takeaway` |
| 10 | CTA | `CTA_Question`, `CTA_Steps` |

## Field names (must match exactly)

### Slide 1 — `Title`
One text box. Pink pill = static design element.

### Body slides — `Body1_` through `Body7_`
| Field | Purpose |
|-------|---------|
| `Body{N}_Heading` | Slide heading |
| `Body{N}_P1` | First paragraph block |
| `Body{N}_P2` | Second paragraph block (merge para 2+3 from template here) |

### Slide 9 — `Takeaway`
One text box. Full statement.

### Slide 10 — `CTA_Question`, `CTA_Steps`
Question box + combined instructions box.

## ⚠️ Canva drops empty columns

Every column you connect needs **some text** in the data row (use a single space ` ` if unused).

## Repeat workflow — CSV copy/paste (simplest)

Field connections stay on the template (purple tags), but you reload data each generate. The fastest reliable path:

1. Agent outputs a **2-row CSV** (row 1 = headers, row 2 = copy) in a `csv` code block
2. Save as `.csv` → open in Google Sheets or Excel
3. Select **row 2 only** (the data row) → copy
4. Open your **Carousel Data** Canva Sheet → click **A2** → paste **values only**
5. Template → **Bulk Create** → **Sheets** → pick Carousel Data → **Generate** → export PNGs

Pasting directly from chat into Canva Sheets does not split columns. The extra 10 seconds to open the CSV file is what makes paste work.

### One-time setup

1. Create a Canva Sheet named `Carousel Data`
2. Row 1 = the 25 column headers (from `carousel-data-headers-only.csv`)
3. Connect template fields once → save template

### Optional: Google Sheet as permanent hub

Same headers in a Google Sheet; paste row 2 from the agent CSV each time; Bulk Create → **Google Sheets** app instead of Canva Sheets. Connections on the template still persist.

## Bulk Create workflow

```
1. Agent outputs CSV (headers + data row)
2. Save → open → copy row 2 → paste values only into Canva Sheet A2
3. Bulk Create → Sheets → Generate
4. Delete unused body slides → export PNGs
```

## Full column order (CSV)

```
Title,Body1_Heading,Body1_P1,Body1_P2,Body2_Heading,Body2_P1,Body2_P2,Body3_Heading,Body3_P1,Body3_P2,Body4_Heading,Body4_P1,Body4_P2,Body5_Heading,Body5_P1,Body5_P2,Body6_Heading,Body6_P1,Body6_P2,Body7_Heading,Body7_P1,Body7_P2,Takeaway,CTA_Question,CTA_Steps
```

**Test files:** `sample-canva-strategy-test.xlsx` | `sample-canva-bulk-create.xlsx` | `carousel-data-headers-only.csv`

## Template tweaks

- Delete yellow PerfectIf boxes from body slides
- Merge title / takeaway / CTA text as documented above
- Size boxes for word-first copy (taller P1/P2 areas)

## Future: Autofill API (Enterprise)

Same 25 field names map 1:1 to autofill keys if you upgrade later.

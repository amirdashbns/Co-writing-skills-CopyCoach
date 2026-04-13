"""
Instagram Carousel: "Your AI content sounds generic. Here's why."
Pillar: AI Writing Done Right
Formula: Educate 5 — Problem Awareness
ICP Pain Point: The Sameness Problem
10 slides, 1080x1350px (4:5 portrait), Hourglass Flow

Design: carousel-design-specs.md
Fonts: Montserrat (variable), DM Sans (variable)
"""

from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1080, 1350
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
FONT_DIR = os.path.join(REPO_ROOT, "context", "design", "fonts")

MONTSERRAT = os.path.join(FONT_DIR, "Montserrat-Variable.ttf")
MONTSERRAT_ITALIC = os.path.join(FONT_DIR, "Montserrat-Italic-Variable.ttf")
DM_SANS = os.path.join(FONT_DIR, "DMSans-Variable.ttf")

# Design spec colors
BG = "#FFF5F0"
TEXT_PRIMARY = "#1A1A1A"
TEXT_ACCENT = "#E63B2E"
HANDLE_COLOR = "#3D2B1F"
ARROW_COLOR = "#3D2B1F"

# Design spec spacing
PAD_TOP = 100
PAD_BOTTOM = 160
PAD_LEFT = 80
PAD_RIGHT = 80
GAP_HEADLINE_BODY = 60
GAP_PARAGRAPH = 40
GAP_BODY_CTA = 60
HANDLE_BOTTOM = 40

CONTENT_WIDTH = WIDTH - PAD_LEFT - PAD_RIGHT


# ── FONT HELPERS ──────────────────────────────────────────────────

def montserrat(size, weight=900):
    """Montserrat variable font. weight: 100-900"""
    f = ImageFont.truetype(MONTSERRAT, size)
    f.set_variation_by_axes([weight])
    return f


def montserrat_italic(size, weight=700):
    f = ImageFont.truetype(MONTSERRAT_ITALIC, size)
    f.set_variation_by_axes([weight])
    return f


def dm_sans(size, weight=400):
    """DM Sans variable font. weight: 100-1000. opsz fixed at 14."""
    f = ImageFont.truetype(DM_SANS, size)
    f.set_variation_by_axes([14, weight])
    return f


# ── DRAWING HELPERS ───────────────────────────────────────────────

def text_height(draw, text, font, spacing=0):
    bb = draw.multiline_textbbox((0, 0), text, font=font, spacing=spacing)
    return bb[3] - bb[1]


def draw_handle(draw):
    f = dm_sans(28, 500)
    handle = "@aicopycoach"
    bb = draw.textbbox((0, 0), handle, font=f)
    tw = bb[2] - bb[0]
    x = (WIDTH - tw) // 2
    y = HEIGHT - HANDLE_BOTTOM - (bb[3] - bb[1])
    draw.text((x, y), handle, font=f, fill=HANDLE_COLOR)


def draw_arrow(draw):
    f = montserrat(48, 700)
    arrow = "\u2192"
    bb = draw.textbbox((0, 0), arrow, font=f)
    x = WIDTH - PAD_RIGHT - (bb[2] - bb[0])
    y = HEIGHT - 180
    draw.text((x, y), arrow, font=f, fill=ARROW_COLOR)


def draw_rich_text(draw, x, y, segments, spacing=0):
    """Draw text with mixed colors. segments = [(text, font, color), ...]
    Each segment is on its own line(s). Returns total height used."""
    cursor_y = y
    for text, fnt, color in segments:
        line_sp = spacing
        draw.multiline_text((x, cursor_y), text, font=fnt, fill=color, spacing=line_sp)
        h = text_height(draw, text, fnt, line_sp)
        cursor_y += h + GAP_PARAGRAPH
    return cursor_y - y


# ── SLIDE CONTENT ─────────────────────────────────────────────────

SLIDES = [
    # SLIDE 1: Cover (TYPE 1)
    {
        "type": "cover",
        "headline": "YOUR AI CONTENT\nSOUNDS GENERIC.",
        "subtitle": "Here's why.",
        "arrow": True,
    },
    # SLIDE 2: Story/Context (TYPE 2) — zoom in
    {
        "type": "story",
        "headline": "You're doing everything\n\"right.\"",
        "body": [
            ("Good prompts. Clear instructions.", TEXT_PRIMARY),
            ("Maybe even a \"write in my brand\nvoice\" at the end.", TEXT_PRIMARY),
            ("So why does it still sound like\neveryone else's?", TEXT_ACCENT),
        ],
    },
    # SLIDE 3: Punch (TYPE 3) — the truth
    {
        "type": "punch",
        "lines": [
            ("AI DOESN'T", TEXT_PRIMARY),
            ("KNOW YOU.", TEXT_ACCENT),
        ],
        "arrow": True,
    },
    # SLIDE 4: Body/Teaching (TYPE 4) — deep zoom
    {
        "type": "body",
        "body": [
            ("\"Write in a casual tone\" is not\ncontext.", TEXT_PRIMARY, True),
            ("YOUR version of casual is\ndifferent from mine.", TEXT_PRIMARY, False),
            ("\"Casual\" to AI means \"corporate\nbut with contractions.\"", TEXT_PRIMARY, False),
            ("Didn't think so\u2026", TEXT_ACCENT, False),
        ],
    },
    # SLIDE 5: Body/Teaching (TYPE 4) — deep zoom
    {
        "type": "body",
        "body": [
            ("Every time you hit \"Generate\" you\nget something grammatically\nperfect.", TEXT_PRIMARY, False),
            ("And completely forgettable.", TEXT_ACCENT, True),
            ("Then you spend 45 minutes editing\nit to not sound like AI.", TEXT_PRIMARY, False),
        ],
    },
    # SLIDE 6: Body/Teaching (TYPE 4) — empathy
    {
        "type": "body",
        "body": [
            ("I get it.", TEXT_PRIMARY, True),
            ("You've tried prompt packs.\nYou've taken a course.\nYou've copy-pasted \"brand\nguidelines\" into ChatGPT.", TEXT_PRIMARY, False),
            ("And it makes sense \u2014 that's what\neveryone teaches.", TEXT_PRIMARY, False),
        ],
    },
    # SLIDE 7: Punch (TYPE 3) — the shift
    {
        "type": "punch",
        "lines": [
            ("PROMPTS TELL AI", TEXT_PRIMARY),
            ("WHAT TO WRITE.", TEXT_PRIMARY),
            ("CONTEXT TEACHES AI", TEXT_PRIMARY),
            ("HOW TO THINK", TEXT_ACCENT),
            ("LIKE YOU.", TEXT_ACCENT),
        ],
        "arrow": True,
    },
    # SLIDE 8: Body/Teaching (TYPE 4) — the fix
    {
        "type": "body",
        "body": [
            ("Instead of better prompts \u2014", TEXT_PRIMARY, True),
            ("Feed AI your actual writing.\nYour sentence patterns.\nYour phrases. Your weird little\nquirks.", TEXT_PRIMARY, False),
            ("THAT'S what kills generic.", TEXT_ACCENT, True),
        ],
    },
    # SLIDE 9: Punch/Takeaway (TYPE 3) — standalone screenshot
    {
        "type": "punch",
        "lines": [
            ("IT'S NOT ABOUT", TEXT_PRIMARY),
            ("THE PROMPT.", TEXT_PRIMARY),
            ("IT'S ABOUT", TEXT_PRIMARY),
            ("THE CONTEXT.", TEXT_ACCENT),
        ],
        "arrow": False,
    },
    # SLIDE 10: CTA (TYPE 5)
    {
        "type": "cta",
        "headline": "I build AI writing\nsystems that sound\nlike YOU.",
        "body": "Not like ChatGPT.\nNot like everyone else.\nLike you.",
        "cta_line": "Comment \"VOICE\" to see how \u2192",
    },
]


# ── SLIDE RENDERERS ───────────────────────────────────────────────

def render_cover(s, idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    d = ImageDraw.Draw(img)

    # Headline: Montserrat Black, 74px, uppercase
    hf = montserrat(74, 900)
    y = PAD_TOP
    head_sp = int(74 * 0.1)
    d.multiline_text((PAD_LEFT, y), s["headline"], font=hf, fill=TEXT_PRIMARY, spacing=head_sp)
    hh = text_height(d, s["headline"], hf, head_sp)

    # Subtitle: Montserrat Bold Italic, 52px
    sf = montserrat_italic(52, 700)
    sy = y + hh + GAP_HEADLINE_BODY
    d.text((PAD_LEFT, sy), s["subtitle"], font=sf, fill=TEXT_PRIMARY)

    if s.get("arrow"):
        draw_arrow(d)
    draw_handle(d)
    return img


def render_story(s, idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    d = ImageDraw.Draw(img)

    # Headline: Montserrat Bold, 56px, sentence case
    hf = montserrat(56, 700)
    y = PAD_TOP
    head_sp = int(56 * 0.1)
    d.multiline_text((PAD_LEFT, y), s["headline"], font=hf, fill=TEXT_PRIMARY, spacing=head_sp)
    hh = text_height(d, s["headline"], hf, head_sp)

    # Body paragraphs: DM Sans Regular, 42px
    bf = dm_sans(42, 400)
    by = y + hh + GAP_HEADLINE_BODY
    body_sp = int(42 * 0.4)
    for text, color in s["body"]:
        d.multiline_text((PAD_LEFT, by), text, font=bf, fill=color, spacing=body_sp)
        bh = text_height(d, text, bf, body_sp)
        by += bh + GAP_PARAGRAPH

    draw_handle(d)
    return img


def render_punch(s, idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    d = ImageDraw.Draw(img)

    hf = montserrat(66, 900)
    y = 120
    line_sp = int(66 * 0.15)
    for text, color in s["lines"]:
        d.text((PAD_LEFT, y), text, font=hf, fill=color)
        bb = d.textbbox((0, 0), text, font=hf)
        y += (bb[3] - bb[1]) + line_sp

    if s.get("arrow"):
        draw_arrow(d)
    draw_handle(d)
    return img


def render_body(s, idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    d = ImageDraw.Draw(img)

    y = PAD_TOP
    body_sp = int(42 * 0.4)
    for text, color, bold in s["body"]:
        fnt = dm_sans(44, 700) if bold else dm_sans(42, 400)
        d.multiline_text((PAD_LEFT, y), text, font=fnt, fill=color, spacing=body_sp)
        h = text_height(d, text, fnt, body_sp)
        y += h + GAP_PARAGRAPH

    draw_handle(d)
    return img


def render_cta(s, idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    d = ImageDraw.Draw(img)

    # Headline: Montserrat Bold, 58px
    hf = montserrat(58, 700)
    y = PAD_TOP
    head_sp = int(58 * 0.1)
    d.multiline_text((PAD_LEFT, y), s["headline"], font=hf, fill=TEXT_PRIMARY, spacing=head_sp)
    hh = text_height(d, s["headline"], hf, head_sp)

    # Body: DM Sans Regular, 40px
    bf = dm_sans(40, 400)
    by = y + hh + GAP_HEADLINE_BODY - 20
    body_sp = int(40 * 0.4)
    d.multiline_text((PAD_LEFT, by), s["body"], font=bf, fill=TEXT_PRIMARY, spacing=body_sp)
    bh = text_height(d, s["body"], bf, body_sp)

    # CTA line: Montserrat Bold, 44px, red accent
    cf = montserrat(44, 700)
    cy = by + bh + GAP_BODY_CTA
    d.text((PAD_LEFT, cy), s["cta_line"], font=cf, fill=TEXT_ACCENT)

    draw_handle(d)
    return img


RENDERERS = {
    "cover": render_cover,
    "story": render_story,
    "punch": render_punch,
    "body": render_body,
    "cta": render_cta,
}


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for idx, s in enumerate(SLIDES):
        img = RENDERERS[s["type"]](s, idx)
        fname = f"slide_{idx + 1:02d}.png"
        img.save(os.path.join(OUTPUT_DIR, fname), "PNG")
        print(f"  {fname}  ({s['type']})")
    print(f"\n  {len(SLIDES)} slides -> {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()

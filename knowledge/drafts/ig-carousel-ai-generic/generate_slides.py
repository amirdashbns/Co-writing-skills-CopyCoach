"""
Instagram Carousel: "Your AI content sounds generic. Here's why."
Pillar: AI Writing Done Right
Formula: Educate 5 — Problem Awareness
ICP Pain Point: The Sameness Problem
10 slides, 1080x1350px (4:5 portrait), Hourglass Flow
"""

from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1080, 1350
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

PALETTE = {
    "bg": "#0D0D0D",
    "bg_alt": "#111111",
    "accent": "#E8A838",
    "white": "#FFFFFF",
    "body": "#C8C8C8",
    "muted": "#777777",
    "tag_bg": "#1A1A1A",
    "divider": "#252525",
    "cta_btn": "#E8A838",
    "cta_btn_text": "#0D0D0D",
}

# ── SLIDE CONTENT (Educate 5 — Problem Awareness) ─────────────────
# Hourglass: Slide 1 zoomed out → 2-3 zoom in → 4-7 deep zoom →
#            8-9 zoom back out → 10 connect to you
SLIDES = [
    {
        "type": "cover",
        "tag": "AI WRITING",
        "headline": "Your AI content\nsounds generic.",
        "sub": "Here's why →",
    },
    {
        "type": "body",
        "num": "01",
        "heading": "You're doing everything\n\"right.\"",
        "body": (
            "Good prompts. Clear instructions.\n"
            "Maybe even a \"write in my brand\n"
            "voice\" at the end.\n\n"
            "So why does it still sound like\n"
            "everyone else's?"
        ),
    },
    {
        "type": "body",
        "num": "02",
        "heading": "The truth is →",
        "body": (
            "AI doesn't know you.\n\n"
            "It doesn't know your quirks.\n"
            "Your humor. Your opinions.\n"
            "The way you start sentences.\n\n"
            "So it defaults to Average."
        ),
    },
    {
        "type": "body",
        "num": "03",
        "heading": "\"Write in a casual tone\"\nis not context.",
        "body": (
            "YOUR version of casual is\n"
            "different from mine.\n\n"
            "\"Casual\" to AI means\n"
            "\"corporate but with\n"
            "contractions.\"\n\n"
            "Didn't think so..."
        ),
    },
    {
        "type": "body",
        "num": "04",
        "heading": "Every time you hit\n\"Generate\" →",
        "body": (
            "You get something grammatically\n"
            "perfect.\n\n"
            "And completely forgettable.\n\n"
            "Then you spend 45 min editing it\n"
            "to not sound like AI."
        ),
    },
    {
        "type": "body",
        "num": "05",
        "heading": "I get it.",
        "body": (
            "You've tried prompt packs.\n"
            "You've taken a course.\n"
            "You've copy-pasted \"brand\n"
            "guidelines\" into ChatGPT.\n\n"
            "And it makes sense —\n"
            "that's what everyone teaches."
        ),
    },
    {
        "type": "body",
        "num": "06",
        "heading": "But here's the thing:",
        "body": (
            "Prompts tell AI what to WRITE.\n\n"
            "Context teaches AI\n"
            "how to THINK like you.\n\n"
            "Completely different game."
        ),
    },
    {
        "type": "body",
        "num": "07",
        "heading": "Instead of better\nprompts, try this →",
        "body": (
            "Feed AI your actual writing.\n"
            "Your sentence patterns.\n"
            "Your phrases. Your weird little\n"
            "quirks.\n\n"
            "THAT'S what kills generic."
        ),
    },
    {
        "type": "takeaway",
        "heading": "It's not about the\nprompt.",
        "sub": "It's about the CONTEXT.",
        "footer": "A perfect prompt with zero context\nstill produces generic output. Every time.",
    },
    {
        "type": "cta",
        "heading": "I build AI writing\nsystems that sound\nlike YOU.",
        "body": "Not like ChatGPT. Not like\neveryone else. Like you.",
        "cta_text": "Comment \"VOICE\" to see how →",
    },
]


def font(path, size):
    return ImageFont.truetype(path, size)


def rounded_rect(draw, xy, r, fill):
    x0, y0, x1, y1 = xy
    draw.rectangle([x0 + r, y0, x1 - r, y1], fill=fill)
    draw.rectangle([x0, y0 + r, x1, y1 - r], fill=fill)
    draw.pieslice([x0, y0, x0 + 2 * r, y0 + 2 * r], 180, 270, fill=fill)
    draw.pieslice([x1 - 2 * r, y0, x1, y0 + 2 * r], 270, 360, fill=fill)
    draw.pieslice([x0, y1 - 2 * r, x0 + 2 * r, y1], 90, 180, fill=fill)
    draw.pieslice([x1 - 2 * r, y1 - 2 * r, x1, y1], 0, 90, fill=fill)


def text_h(draw, text, f):
    bb = draw.multiline_textbbox((0, 0), text, font=f)
    return bb[3] - bb[1]


def accent_bar(draw, x, y, h):
    rounded_rect(draw, (x, y, x + 5, y + h), 2, PALETTE["accent"])


def swipe_dots(draw, current, total):
    r = 5
    gap = 22
    total_w = total * r * 2 + (total - 1) * (gap - r * 2)
    sx = (WIDTH - total_w) // 2
    y = HEIGHT - 65
    for i in range(total):
        cx = sx + i * gap + r
        c = PALETTE["accent"] if i == current else PALETTE["divider"]
        draw.ellipse([cx - r, y - r, cx + r, y + r], fill=c)


def top_bar(draw, thick=4):
    draw.rectangle([0, 0, WIDTH, thick], fill=PALETTE["accent"])


def slide_num(draw, num):
    f = font(FONT_BOLD, 24)
    draw.text((80, 75), num, font=f, fill=PALETTE["accent"])


# ── SLIDE RENDERERS ───────────────────────────────────────────────

def render_cover(s, idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), PALETTE["bg"])
    d = ImageDraw.Draw(img)
    top_bar(d, 6)

    # tag pill
    tf = font(FONT_BOLD, 24)
    tag = s["tag"]
    tb = d.textbbox((0, 0), tag, font=tf)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    tx, ty = 80, 140
    rounded_rect(d, (tx - 14, ty - 8, tx + tw + 14, ty + th + 8), 6, PALETTE["tag_bg"])
    d.text((tx, ty), tag, font=tf, fill=PALETTE["accent"])

    # headline
    hf = font(FONT_BOLD, 86)
    hy = 300
    for line in s["headline"].split("\n"):
        d.text((80, hy), line, font=hf, fill=PALETTE["white"])
        lb = d.textbbox((0, 0), line, font=hf)
        hy += (lb[3] - lb[1]) + 18

    # accent dash
    d.rectangle([80, hy + 30, 160, hy + 35], fill=PALETTE["accent"])

    # sub
    sf = font(FONT_BOLD, 42)
    d.text((80, hy + 65), s["sub"], font=sf, fill=PALETTE["accent"])

    swipe_dots(d, idx, len(SLIDES))
    return img


def render_body(s, idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), PALETTE["bg_alt"])
    d = ImageDraw.Draw(img)
    top_bar(d)
    slide_num(d, s["num"])

    # heading with accent bar
    hf = font(FONT_BOLD, 56)
    hy = 155
    hh = text_h(d, s["heading"], hf)
    accent_bar(d, 80, hy + 4, hh)
    d.multiline_text((100, hy), s["heading"], font=hf, fill=PALETTE["white"], spacing=12)

    # divider
    div_y = hy + hh + 50
    d.rectangle([80, div_y, WIDTH - 80, div_y + 2], fill=PALETTE["divider"])

    # body
    bf = font(FONT_REGULAR, 34)
    d.multiline_text((80, div_y + 30), s["body"], font=bf, fill=PALETTE["body"], spacing=14)

    swipe_dots(d, idx, len(SLIDES))
    return img


def render_takeaway(s, idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), PALETTE["bg"])
    d = ImageDraw.Draw(img)
    top_bar(d, 6)

    # heading
    hf = font(FONT_BOLD, 68)
    hy = 280
    hh = text_h(d, s["heading"], hf)
    d.multiline_text((80, hy), s["heading"], font=hf, fill=PALETTE["white"], spacing=14)

    # accent sub
    sf = font(FONT_BOLD, 68)
    sy = hy + hh + 30
    d.multiline_text((80, sy), s["sub"], font=sf, fill=PALETTE["accent"], spacing=14)

    # divider
    sh = text_h(d, s["sub"], sf)
    div_y = sy + sh + 50
    d.rectangle([80, div_y, WIDTH - 80, div_y + 2], fill=PALETTE["divider"])

    # footer
    ff = font(FONT_REGULAR, 32)
    d.multiline_text((80, div_y + 30), s["footer"], font=ff, fill=PALETTE["muted"], spacing=12)

    swipe_dots(d, idx, len(SLIDES))
    return img


def render_cta(s, idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), PALETTE["bg"])
    d = ImageDraw.Draw(img)
    top_bar(d, 6)

    # heading
    hf = font(FONT_BOLD, 64)
    hy = 250
    hh = text_h(d, s["heading"], hf)
    d.multiline_text((80, hy), s["heading"], font=hf, fill=PALETTE["white"], spacing=14)

    # dash
    d.rectangle([80, hy + hh + 40, 160, hy + hh + 45], fill=PALETTE["accent"])

    # body
    bf = font(FONT_REGULAR, 34)
    by = hy + hh + 80
    d.multiline_text((80, by), s["body"], font=bf, fill=PALETTE["muted"], spacing=12)
    bh = text_h(d, s["body"], bf)

    # button
    btf = font(FONT_BOLD, 32)
    bt = s["cta_text"]
    bb = d.textbbox((0, 0), bt, font=btf)
    bw, bh2 = bb[2] - bb[0], bb[3] - bb[1]
    px, py = 44, 20
    bx = (WIDTH - bw - 2 * px) // 2
    btn_y = by + bh + 80
    rounded_rect(d, (bx, btn_y, bx + bw + 2 * px, btn_y + bh2 + 2 * py), 10, PALETTE["cta_btn"])
    d.text((bx + px, btn_y + py), bt, font=btf, fill=PALETTE["cta_btn_text"])

    swipe_dots(d, idx, len(SLIDES))
    return img


RENDERERS = {
    "cover": render_cover,
    "body": render_body,
    "takeaway": render_takeaway,
    "cta": render_cta,
}


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for idx, s in enumerate(SLIDES):
        img = RENDERERS[s["type"]](s, idx)
        fname = f"slide_{idx + 1:02d}.png"
        img.save(os.path.join(OUTPUT_DIR, fname), "PNG")
        print(f"  {fname}  ({s['type']})")
    print(f"\n  {len(SLIDES)} slides → {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()

"""
Generate 7-slide Instagram carousel: "Why AI Content Sounds Generic"
Framework: Problem → Agitate → Solve (adapted to 7 slides)
Dimensions: 1080x1350px (4:5 portrait)
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

WIDTH, HEIGHT = 1080, 1350
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

COLORS = {
    "bg_dark": "#0F0F0F",
    "bg_body": "#141414",
    "accent": "#D4A843",
    "headline": "#FFFFFF",
    "body": "#CCCCCC",
    "muted": "#888888",
    "tag_bg": "#1E1E1E",
    "divider": "#2A2A2A",
    "cta_bg": "#D4A843",
    "cta_text": "#0F0F0F",
}

SLIDES = [
    {
        "type": "cover",
        "tag": "AI CONTENT",
        "headline": "Why your\nAI content\nsounds like\neveryone else's",
        "subheadline": "And the 3 fixes that change everything.",
    },
    {
        "type": "problem",
        "slide_num": "01",
        "headline": "The problem\nisn't AI.",
        "body": (
            "You paste a prompt into ChatGPT.\n\n"
            "You get back something that's\n"
            "grammatically perfect, structurally\n"
            "sound — and completely forgettable.\n\n"
            "It reads like it could've been\n"
            "written by anyone. Because it was\n"
            "written by no one."
        ),
    },
    {
        "type": "agitate",
        "slide_num": "02",
        "headline": "Generic content\ncosts you more\nthan you think.",
        "body": (
            "Your audience scrolls past it.\n"
            "Algorithms bury it.\n"
            "Competitors publish the same thing.\n\n"
            "The result?\n"
            "Zero trust. Zero engagement.\n"
            "Zero growth."
        ),
    },
    {
        "type": "solve",
        "slide_num": "03",
        "headline": "Fix #1\nFeed it your voice.",
        "body": (
            "AI doesn't know how you talk.\n\n"
            "Give it 5–10 samples of your\n"
            "best writing. Tell it your tone,\n"
            "your phrases, your quirks.\n\n"
            "The output goes from \"AI wrote this\"\n"
            "to \"this sounds like me.\""
        ),
    },
    {
        "type": "solve",
        "slide_num": "04",
        "headline": "Fix #2\nStop asking for\nfinal drafts.",
        "body": (
            "\"Write me a LinkedIn post\" is a\n"
            "terrible prompt.\n\n"
            "Instead: ask for 5 angles.\n"
            "Pick the best one.\n"
            "Then build from there.\n\n"
            "Treat AI as a brainstorm partner,\n"
            "not a ghostwriter."
        ),
    },
    {
        "type": "solve",
        "slide_num": "05",
        "headline": "Fix #3\nAdd what AI\ncan't invent.",
        "body": (
            "AI can't tell your stories.\n"
            "It doesn't have your opinions.\n"
            "It hasn't made your mistakes.\n\n"
            "Inject your lived experience.\n"
            "That's the layer no one\n"
            "can replicate — and the one\n"
            "your audience actually wants."
        ),
    },
    {
        "type": "cta",
        "headline": "AI is a tool.\nYour voice is\nthe strategy.",
        "body": "Save this for your next content session.",
        "cta_text": "FOLLOW FOR MORE",
    },
]


def load_font(path, size):
    return ImageFont.truetype(path, size)


def draw_rounded_rect(draw, xy, radius, fill):
    x0, y0, x1, y1 = xy
    draw.rectangle([x0 + radius, y0, x1 - radius, y1], fill=fill)
    draw.rectangle([x0, y0 + radius, x1, y1 - radius], fill=fill)
    draw.pieslice([x0, y0, x0 + 2 * radius, y0 + 2 * radius], 180, 270, fill=fill)
    draw.pieslice([x1 - 2 * radius, y0, x1, y0 + 2 * radius], 270, 360, fill=fill)
    draw.pieslice([x0, y1 - 2 * radius, x0 + 2 * radius, y1], 90, 180, fill=fill)
    draw.pieslice([x1 - 2 * radius, y1 - 2 * radius, x1, y1], 0, 90, fill=fill)


def get_text_height(draw, text, font):
    bbox = draw.multiline_textbbox((0, 0), text, font=font)
    return bbox[3] - bbox[1]


def draw_accent_bar(draw, x, y, height):
    draw_rounded_rect(draw, (x, y, x + 6, y + height), 3, COLORS["accent"])


def draw_slide_number(draw, num):
    font = load_font(FONT_BOLD, 28)
    draw.text((80, 80), num, font=font, fill=COLORS["accent"])


def draw_swipe_indicator(draw, current, total):
    dot_radius = 6
    spacing = 24
    total_width = total * (dot_radius * 2) + (total - 1) * (spacing - dot_radius * 2)
    start_x = (WIDTH - total_width) // 2
    y = HEIGHT - 70

    for i in range(total):
        cx = start_x + i * spacing + dot_radius
        if i == current:
            draw.ellipse(
                [cx - dot_radius, y - dot_radius, cx + dot_radius, y + dot_radius],
                fill=COLORS["accent"],
            )
        else:
            draw.ellipse(
                [cx - dot_radius, y - dot_radius, cx + dot_radius, y + dot_radius],
                fill=COLORS["divider"],
            )


def generate_cover(slide_data, idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg_dark"])
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, WIDTH, 8], fill=COLORS["accent"])

    tag_font = load_font(FONT_BOLD, 26)
    tag_text = slide_data["tag"]
    tag_bbox = draw.textbbox((0, 0), tag_text, font=tag_font)
    tag_w = tag_bbox[2] - tag_bbox[0]
    tag_h = tag_bbox[3] - tag_bbox[1]
    tag_x, tag_y = 80, 120
    draw_rounded_rect(
        draw,
        (tag_x - 16, tag_y - 10, tag_x + tag_w + 16, tag_y + tag_h + 10),
        8,
        COLORS["tag_bg"],
    )
    draw.text((tag_x, tag_y), tag_text, font=tag_font, fill=COLORS["accent"])

    headline_font = load_font(FONT_BOLD, 82)
    headline_y = 260
    for line in slide_data["headline"].split("\n"):
        draw.text((80, headline_y), line, font=headline_font, fill=COLORS["headline"])
        line_bbox = draw.textbbox((0, 0), line, font=headline_font)
        headline_y += (line_bbox[3] - line_bbox[1]) + 20

    draw.rectangle([80, headline_y + 30, 180, headline_y + 36], fill=COLORS["accent"])

    sub_font = load_font(FONT_REGULAR, 36)
    draw.text(
        (80, headline_y + 70),
        slide_data["subheadline"],
        font=sub_font,
        fill=COLORS["muted"],
    )

    draw_swipe_indicator(draw, idx, 7)
    return img


def generate_body_slide(slide_data, idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg_body"])
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, WIDTH, 4], fill=COLORS["accent"])

    draw_slide_number(draw, slide_data["slide_num"])

    headline_font = load_font(FONT_BOLD, 64)
    headline_y = 160
    headline_text = slide_data["headline"]
    headline_height = get_text_height(draw, headline_text, headline_font)
    draw_accent_bar(draw, 80, headline_y + 6, headline_height)
    draw.multiline_text(
        (104, headline_y),
        headline_text,
        font=headline_font,
        fill=COLORS["headline"],
        spacing=14,
    )

    body_top = headline_y + headline_height + 70
    draw.rectangle([80, body_top - 20, WIDTH - 80, body_top - 18], fill=COLORS["divider"])

    body_font = load_font(FONT_REGULAR, 36)
    draw.multiline_text(
        (80, body_top + 10),
        slide_data["body"],
        font=body_font,
        fill=COLORS["body"],
        spacing=16,
    )

    draw_swipe_indicator(draw, idx, 7)
    return img


def generate_cta_slide(slide_data, idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg_dark"])
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, WIDTH, 8], fill=COLORS["accent"])

    headline_font = load_font(FONT_BOLD, 72)
    headline_text = slide_data["headline"]
    headline_y = 280
    headline_height = get_text_height(draw, headline_text, headline_font)
    draw.multiline_text(
        (80, headline_y),
        headline_text,
        font=headline_font,
        fill=COLORS["headline"],
        spacing=16,
    )

    draw.rectangle(
        [80, headline_y + headline_height + 50, 180, headline_y + headline_height + 56],
        fill=COLORS["accent"],
    )

    body_font = load_font(FONT_REGULAR, 36)
    draw.text(
        (80, headline_y + headline_height + 90),
        slide_data["body"],
        font=body_font,
        fill=COLORS["muted"],
    )

    btn_font = load_font(FONT_BOLD, 34)
    btn_text = slide_data["cta_text"]
    btn_bbox = draw.textbbox((0, 0), btn_text, font=btn_font)
    btn_w = btn_bbox[2] - btn_bbox[0]
    btn_h = btn_bbox[3] - btn_bbox[1]
    btn_pad_x, btn_pad_y = 50, 22
    btn_x = (WIDTH - btn_w - 2 * btn_pad_x) // 2
    btn_y = headline_y + headline_height + 200
    draw_rounded_rect(
        draw,
        (btn_x, btn_y, btn_x + btn_w + 2 * btn_pad_x, btn_y + btn_h + 2 * btn_pad_y),
        12,
        COLORS["cta_bg"],
    )
    draw.text(
        (btn_x + btn_pad_x, btn_y + btn_pad_y),
        btn_text,
        font=btn_font,
        fill=COLORS["cta_text"],
    )

    draw_swipe_indicator(draw, idx, 7)
    return img


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for idx, slide_data in enumerate(SLIDES):
        if slide_data["type"] == "cover":
            img = generate_cover(slide_data, idx)
        elif slide_data["type"] == "cta":
            img = generate_cta_slide(slide_data, idx)
        else:
            img = generate_body_slide(slide_data, idx)

        filename = f"slide_{idx + 1:02d}.png"
        filepath = os.path.join(OUTPUT_DIR, filename)
        img.save(filepath, "PNG")
        print(f"Generated: {filename}")

    print(f"\nAll 7 slides saved to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()

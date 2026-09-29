#!/usr/bin/env python3
"""
Add The Office agent labels to a Build-Measure-Learn loop image.

Usage:
    python add_agents_to_loop.py input_image.png output_image.png
"""

import sys
from PIL import Image, ImageDraw, ImageFont
import os


def add_agent_labels(input_path, output_path):
    """Add agent labels to the BML loop image"""

    # Open the image
    img = Image.open(input_path)
    width, height = img.size

    # Create a drawing context
    draw = ImageDraw.Draw(img)

    # Try to use a nice font, fall back to default if not available
    try:
        # Try to find a system font
        font_large = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
        font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
    except:
        try:
            font_large = ImageFont.truetype("Arial.ttf", 48)
            font_medium = ImageFont.truetype("Arial.ttf", 32)
            font_small = ImageFont.truetype("Arial.ttf", 24)
        except:
            # Use default font
            font_large = ImageFont.load_default()
            font_medium = ImageFont.load_default()
            font_small = ImageFont.load_default()

    # Calculate positions based on image size
    center_x = width // 2
    center_y = height // 2

    # Add agent badges as rounded rectangles with text

    # BUILD badge (near top)
    build_x = center_x
    build_y = int(height * 0.38)
    badge_text = "👥 CPO + ⚙️ CTO"
    draw_badge(draw, build_x, build_y, badge_text, font_small, "#3498DB")

    # MEASURE badge (bottom right)
    measure_x = int(width * 0.75)
    measure_y = int(height * 0.75)
    badge_text = "⚙️ CTO + 👥 CPO"
    draw_badge(draw, measure_x, measure_y, badge_text, font_small, "#F1C40F")

    # LEARN badge (bottom left)
    learn_x = int(width * 0.25)
    learn_y = int(height * 0.75)
    badge_text = "📊 CEO + Team"
    draw_badge(draw, learn_x, learn_y, badge_text, font_small, "#2ECC71")

    # Center text
    center_text = "THE OFFICE"
    draw_centered_text(draw, center_x, center_y - 30, center_text, font_large, "#2C3E50")

    sub_text = "AUTONOMOUS"
    draw_centered_text(draw, center_x, center_y + 30, sub_text, font_medium, "#3498DB")

    # Save the result
    img.save(output_path)
    print(f"✅ Saved to {output_path}")


def draw_badge(draw, x, y, text, font, color):
    """Draw a badge with rounded rectangle background"""
    # Get text size
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Badge dimensions
    padding = 20
    badge_width = text_width + padding * 2
    badge_height = text_height + padding * 2

    # Badge position (centered on x, y)
    left = x - badge_width // 2
    top = y - badge_height // 2
    right = left + badge_width
    bottom = top + badge_height

    # Draw rounded rectangle background
    radius = badge_height // 2
    draw.rounded_rectangle(
        [left, top, right, bottom],
        radius=radius,
        fill="white",
        outline=color,
        width=4
    )

    # Draw text centered in badge
    text_x = x - text_width // 2
    text_y = y - text_height // 2
    draw.text((text_x, text_y), text, fill=color, font=font)


def draw_centered_text(draw, x, y, text, font, color):
    """Draw centered text"""
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x = x - text_width // 2
    text_y = y - text_height // 2

    draw.text((text_x, text_y), text, fill=color, font=font)


def main():
    if len(sys.argv) != 3:
        print("Usage: python add_agents_to_loop.py input_image.png output_image.png")
        print("\nExample:")
        print("  python add_agents_to_loop.py lean_startup.png office_loop.png")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.exists(input_path):
        print(f"❌ Error: Input file '{input_path}' not found")
        sys.exit(1)

    print(f"📝 Adding agent labels to {input_path}...")
    add_agent_labels(input_path, output_path)
    print("✅ Done!")


if __name__ == "__main__":
    main()

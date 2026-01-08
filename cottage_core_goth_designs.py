#!/usr/bin/env python3
"""
Cottage Core Goth T-Shirt Design Variants

Uses the CPO agent to design specific variants for the
"Cottage Core Goth" / Aesthetic Mashups trend.
"""

import os
from dotenv import load_dotenv
from src.business import Business

# Load environment
load_dotenv()

if not os.getenv("ANTHROPIC_API_KEY"):
    print("Error: ANTHROPIC_API_KEY not found. Please set it in .env file")
    exit(1)

print("=" * 80)
print("COTTAGE CORE GOTH T-SHIRT DESIGN SESSION")
print("=" * 80)
print()

# Initialize business
business = Business()
cpo = business.get_agent("CPO")

print("CPO is designing Cottage Core Goth t-shirt variants...")
print("-" * 80)
print()

# Have CPO design the variants
design_variants = cpo.think("""
Design 3-4 specific t-shirt variants for the "Cottage Core Goth" / Aesthetic Mashups trend.

This trend combines seemingly opposite aesthetics:
- Cottage Core (soft, pastoral, vintage, florals, mushrooms, nature)
- Goth (dark, moody, skulls, occult, Victorian)

Target Audience:
- Age: 16-28
- Demographics: 65% female, fashion-forward, chronically online
- Values: Individuality, anti-mainstream, aesthetic expression
- Platforms: Pinterest, Instagram, TikTok

For each variant, provide:

1. **Design Name & Concept**
   - Catchy name
   - Core aesthetic fusion

2. **Visual Description**
   - Main graphic elements
   - Color palette (specific colors)
   - Typography style
   - Placement on shirt
   - Overall vibe/mood

3. **Design Elements**
   - Specific imagery (be detailed)
   - Text/phrases (if any)
   - Artistic style (illustration, minimalist, vintage print, etc.)

4. **Target Sub-Audience**
   - Which specific aesthetic community
   - Age range within 16-28
   - Style preferences

5. **Price Point**
   - Recommended retail price
   - Justification

6. **Production Notes**
   - Print complexity (1-color, multi-color, all-over print)
   - Any special techniques needed

Create designs that are:
- Visually striking and Instagram-worthy
- Authentically blend both aesthetics (not just one or the other)
- Wearable as statement pieces
- Appropriate for print-on-demand production
- Fresh takes on the trend (avoid clichés)

Be creative and specific with visual details!
""")

print(design_variants)
print()
print("=" * 80)
print()

# Save to file
print("Saving design variants to file...")
with open("/home/user/the-office/COTTAGE_CORE_GOTH_DESIGNS.md", "w") as f:
    f.write("# Cottage Core Goth T-Shirt Design Variants\n\n")
    f.write("*Designed by CPO Agent*\n\n")
    f.write("**Trend:** Aesthetic Mashups - Cottage Core × Goth\n\n")
    f.write("---\n\n")
    f.write(design_variants)
    f.write("\n\n---\n\n")
    f.write("## Design Philosophy\n\n")
    f.write("These designs blend the soft, pastoral aesthetic of Cottage Core ")
    f.write("with the dark, moody elements of Goth culture, creating a unique ")
    f.write("visual language that appeals to Gen Z's rejection of strict aesthetic ")
    f.write("categories. Each design is carefully crafted to be both wearable and ")
    f.write("Instagram-worthy, targeting the fashion-forward, chronically online ")
    f.write("demographic that values individuality and creative expression.\n")

print("✓ Design variants saved to: COTTAGE_CORE_GOTH_DESIGNS.md")
print()
print("Design session complete!")

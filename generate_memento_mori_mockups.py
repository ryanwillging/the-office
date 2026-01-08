#!/usr/bin/env python3
"""
Generate Memento Mori Garden t-shirt mockups with various color combinations
"""

import os

# Create mockups directory
os.makedirs("designs/mockups", exist_ok=True)

def create_tshirt_template(shirt_color, shirt_color_name):
    """Create base t-shirt template SVG"""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 1000">
  <defs>
    <!-- Shadow filter -->
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.3"/>
    </filter>
    <!-- Fabric texture -->
    <pattern id="fabric" x="0" y="0" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="4" fill="{shirt_color}"/>
      <circle cx="2" cy="2" r="0.3" fill="rgba(0,0,0,0.05)"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="800" height="1000" fill="#f5f5f0"/>

  <!-- T-shirt body -->
  <g filter="url(#shadow)">
    <!-- Main body -->
    <path d="M 200 150 L 200 800 Q 200 850 250 850 L 550 850 Q 600 850 600 800 L 600 150 Z"
          fill="url(#fabric)" stroke="#333" stroke-width="1"/>

    <!-- Sleeves -->
    <path d="M 200 150 L 150 180 L 150 280 L 200 300 Z"
          fill="url(#fabric)" stroke="#333" stroke-width="1"/>
    <path d="M 600 150 L 650 180 L 650 280 L 600 300 Z"
          fill="url(#fabric)" stroke="#333" stroke-width="1"/>

    <!-- Neckline -->
    <ellipse cx="400" cy="150" rx="60" ry="30"
             fill="{shirt_color}" stroke="#333" stroke-width="1"/>

    <!-- Ribbing details -->
    <line x1="250" y1="850" x2="550" y2="850" stroke="#333" stroke-width="0.5" opacity="0.3"/>
    <line x1="150" y1="280" x2="200" y2="300" stroke="#333" stroke-width="0.5" opacity="0.3"/>
    <line x1="650" y1="280" x2="600" y2="300" stroke="#333" stroke-width="0.5" opacity="0.3"/>
  </g>
</svg>'''

def create_memento_mori_variant(design_colors, is_back=False):
    """Create design in specified colors"""
    skull_color = design_colors['skull']
    flower_color = design_colors['flowers']
    accent_color = design_colors['accent']
    moon_color = design_colors['moon']
    text_color = design_colors['text']

    # Back design is larger and centered higher
    if is_back:
        design_x = 400
        design_y = 380
        scale = 1.4
        view_box = "0 0 800 1000"
    else:
        design_x = 400
        design_y = 450
        scale = 1.0
        view_box = "0 0 800 1000"

    return f'''
  <!-- Design placement ({"BACK" if is_back else "FRONT"}) -->
  <g transform="translate({design_x}, {design_y}) scale({scale})">
    <!-- Moon phases arc (top) -->
    <g transform="translate(0, -120)">
      <!-- New moon -->
      <circle cx="-80" cy="0" r="8" fill="none" stroke="{moon_color}" stroke-width="1.5"/>
      <!-- Waxing crescent -->
      <circle cx="-40" cy="-5" r="8" fill="{moon_color}" opacity="0.3"/>
      <path d="M -45,-5 A 8,8 0 0,1 -45,3 A 5,8 0 0,0 -45,-5" fill="{moon_color}"/>
      <!-- Full moon -->
      <circle cx="0" cy="-8" r="10" fill="{moon_color}"/>
      <!-- Waning crescent -->
      <circle cx="40" cy="-5" r="8" fill="{moon_color}" opacity="0.3"/>
      <path d="M 45,-5 A 8,8 0 0,0 45,3 A 5,8 0 0,1 45,-5" fill="{moon_color}"/>
      <!-- New moon -->
      <circle cx="80" cy="0" r="8" fill="none" stroke="{moon_color}" stroke-width="1.5"/>
    </g>

    <!-- Main skull (side profile) -->
    <g transform="translate(-10, 0)">
      <!-- Cranium -->
      <ellipse cx="0" cy="-20" rx="45" ry="50" fill="{skull_color}" stroke="{text_color}" stroke-width="2"/>

      <!-- Forehead slope -->
      <path d="M -30,-50 Q -40,-30 -42,0" fill="{skull_color}" stroke="{text_color}" stroke-width="2"/>

      <!-- Eye socket -->
      <ellipse cx="-15" cy="-15" rx="18" ry="22" fill="{accent_color}" opacity="0.3" stroke="{text_color}" stroke-width="2"/>

      <!-- Nasal cavity -->
      <path d="M -35,0 L -42,10 L -35,15 Z" fill="{accent_color}" opacity="0.3" stroke="{text_color}" stroke-width="2"/>

      <!-- Maxilla (upper jaw) -->
      <path d="M -42,15 Q -45,20 -45,25 L -38,25" fill="{skull_color}" stroke="{text_color}" stroke-width="2"/>

      <!-- Teeth (upper) -->
      <rect x="-45" y="25" width="5" height="8" fill="{skull_color}" stroke="{text_color}" stroke-width="1"/>
      <rect x="-40" y="25" width="5" height="8" fill="{skull_color}" stroke="{text_color}" stroke-width="1"/>
      <rect x="-35" y="25" width="5" height="8" fill="{skull_color}" stroke="{text_color}" stroke-width="1"/>

      <!-- Mandible (lower jaw) -->
      <path d="M -45,33 L -38,33 Q -35,33 -35,36 L -38,45 Q -42,48 -48,45 Q -50,40 -48,35 Z"
            fill="{skull_color}" stroke="{text_color}" stroke-width="2"/>

      <!-- Teeth (lower) -->
      <rect x="-45" y="33" width="5" height="6" fill="{skull_color}" stroke="{text_color}" stroke-width="1"/>
      <rect x="-40" y="33" width="5" height="6" fill="{skull_color}" stroke="{text_color}" stroke-width="1"/>

      <!-- Anatomical details -->
      <path d="M -25,-45 Q -20,-43 -18,-40" stroke="{text_color}" stroke-width="1" fill="none" opacity="0.5"/>
      <path d="M -10,-55 Q -5,-53 0,-50" stroke="{text_color}" stroke-width="1" fill="none" opacity="0.5"/>
      <circle cx="-8" cy="-35" r="2" fill="{text_color}" opacity="0.3"/>

      <!-- Suture lines -->
      <path d="M 20,-30 Q 15,-25 10,-20" stroke="{text_color}" stroke-width="0.8" fill="none" opacity="0.4" stroke-dasharray="2,2"/>
    </g>

    <!-- Wildflowers growing from skull -->
    <!-- Lavender sprigs (from eye socket) -->
    <g transform="translate(-15, -15)">
      <line x1="0" y1="0" x2="-5" y2="-35" stroke="{accent_color}" stroke-width="2"/>
      <circle cx="-5" cy="-38" r="2.5" fill="{flower_color}"/>
      <circle cx="-6" cy="-42" r="2.5" fill="{flower_color}"/>
      <circle cx="-4" cy="-46" r="2.5" fill="{flower_color}"/>
      <line x1="0" y1="0" x2="3" y2="-32" stroke="{accent_color}" stroke-width="2"/>
      <circle cx="3" cy="-35" r="2.5" fill="{flower_color}"/>
      <circle cx="2" cy="-39" r="2.5" fill="{flower_color}"/>
    </g>

    <!-- Roses (from cranium) -->
    <g transform="translate(10, -35)">
      <line x1="0" y1="0" x2="5" y2="-28" stroke="{accent_color}" stroke-width="2.5"/>
      <!-- Rose bloom -->
      <circle cx="5" cy="-30" r="6" fill="{flower_color}" opacity="0.8"/>
      <circle cx="5" cy="-30" r="4" fill="{flower_color}"/>
      <circle cx="5" cy="-30" r="2" fill="{accent_color}" opacity="0.6"/>
      <!-- Leaves -->
      <ellipse cx="2" cy="-20" rx="4" ry="6" fill="{accent_color}" opacity="0.7" transform="rotate(-30, 2, -20)"/>
      <ellipse cx="7" cy="-15" rx="4" ry="6" fill="{accent_color}" opacity="0.7" transform="rotate(20, 7, -15)"/>
    </g>

    <!-- Forget-me-nots cluster (from cranium top) -->
    <g transform="translate(-5, -55)">
      <line x1="0" y1="0" x2="-3" y2="-18" stroke="{accent_color}" stroke-width="1.5"/>
      <!-- 5-petal flowers -->
      <g transform="translate(-3, -20)">
        <circle cx="0" cy="0" r="4" fill="{flower_color}"/>
        <circle cx="-3" cy="-2" r="1.5" fill="{moon_color}"/>
        <circle cx="3" cy="-2" r="1.5" fill="{moon_color}"/>
        <circle cx="-2" cy="3" r="1.5" fill="{moon_color}"/>
        <circle cx="2" cy="3" r="1.5" fill="{moon_color}"/>
        <circle cx="0" cy="-4" r="1.5" fill="{moon_color}"/>
        <circle cx="0" cy="0" r="1" fill="#FFD700"/>
      </g>
      <g transform="translate(-7, -15)">
        <circle cx="0" cy="0" r="3.5" fill="{flower_color}"/>
        <circle cx="-2" cy="-1.5" r="1.3" fill="{moon_color}"/>
        <circle cx="2" cy="-1.5" r="1.3" fill="{moon_color}"/>
        <circle cx="-1.5" cy="2.5" r="1.3" fill="{moon_color}"/>
        <circle cx="1.5" cy="2.5" r="1.3" fill="{moon_color}"/>
        <circle cx="0" cy="-3.5" r="1.3" fill="{moon_color}"/>
        <circle cx="0" cy="0" r="0.8" fill="#FFD700"/>
      </g>
    </g>

    <!-- Wild daisies (from jaw area) -->
    <g transform="translate(-35, 20)">
      <line x1="0" y1="0" x2="8" y2="-22" stroke="{accent_color}" stroke-width="1.8"/>
      <g transform="translate(8, -24)">
        <circle cx="0" cy="0" r="5" fill="{skull_color}"/>
        <ellipse cx="-4" cy="0" rx="2" ry="4" fill="{skull_color}"/>
        <ellipse cx="4" cy="0" rx="2" ry="4" fill="{skull_color}"/>
        <ellipse cx="0" cy="-4" rx="4" ry="2" fill="{skull_color}"/>
        <ellipse cx="0" cy="4" rx="4" ry="2" fill="{skull_color}"/>
        <circle cx="0" cy="0" r="2" fill="#FFD700"/>
      </g>
    </g>

    <!-- Small snail detail -->
    <g transform="translate(30, 40)">
      <ellipse cx="0" cy="0" rx="4" ry="3" fill="{accent_color}" opacity="0.6"/>
      <circle cx="-2" cy="-2" r="3" fill="{flower_color}" opacity="0.5"/>
      <path d="M -2,-2 Q 0,-4 2,-2" stroke="{text_color}" stroke-width="0.8" fill="none"/>
      <line x1="0" y1="2" x2="-1" y2="5" stroke="{text_color}" stroke-width="0.6"/>
      <line x1="2" y1="2" x2="3" y2="5" stroke="{text_color}" stroke-width="0.6"/>
    </g>

    <!-- Roots at bottom -->
    <g transform="translate(-10, 50)">
      <path d="M 0,0 Q -5,8 -8,15 Q -10,20 -12,28" stroke="{accent_color}" stroke-width="1.5" fill="none" opacity="0.7"/>
      <path d="M 0,0 Q 2,10 0,18 Q -2,25 0,32" stroke="{accent_color}" stroke-width="1.5" fill="none" opacity="0.7"/>
      <path d="M 0,0 Q 5,7 8,14 Q 10,22 8,30" stroke="{accent_color}" stroke-width="1.5" fill="none" opacity="0.7"/>
    </g>

    <!-- Quote text (bottom) -->
    <text x="0" y="95" font-family="Georgia, serif" font-size="11" fill="{text_color}"
          text-anchor="middle" font-style="italic" opacity="0.9">
      From death, life blooms
    </text>
  </g>'''

# Color combinations for popular t-shirt colors
color_combinations = {
    "black": {
        "name": "Midnight Garden (Black)",
        "shirt": "#1a1a1a",
        "design": {
            "skull": "#FFF8DC",
            "flowers": "#C8A2C8",
            "accent": "#9CAF88",
            "moon": "#E8DCC4",
            "text": "#D4C4A8"
        },
        "description": "Classic goth aesthetic with soft lavender and sage accents"
    },
    "cream": {
        "name": "Bone Garden (Natural)",
        "shirt": "#F5F5DC",
        "design": {
            "skull": "#2C3539",
            "flowers": "#8B5A8B",
            "accent": "#4A5D23",
            "moon": "#5A5A5A",
            "text": "#1a1a1a"
        },
        "description": "Cottage core vibes with dark botanical elements"
    },
    "forest": {
        "name": "Woodland Memento (Forest Green)",
        "shirt": "#2d4a2b",
        "design": {
            "skull": "#FFF8DC",
            "flowers": "#DDA0DD",
            "accent": "#C8D5B9",
            "moon": "#FAF0E6",
            "text": "#E8DCC4"
        },
        "description": "Deep forest base with ethereal light florals"
    },
    "burgundy": {
        "name": "Gothic Romance (Burgundy)",
        "shirt": "#6B2737",
        "design": {
            "skull": "#FFF5EE",
            "flowers": "#E6C9E6",
            "accent": "#B5C9A4",
            "moon": "#FFE4E1",
            "text": "#F4E8D8"
        },
        "description": "Rich wine tones with romantic pastels"
    },
    "charcoal": {
        "name": "Modern Memento (Charcoal)",
        "shirt": "#36454F",
        "design": {
            "skull": "#FFF8DC",
            "flowers": "#C8A2C8",
            "accent": "#A8B5A0",
            "moon": "#E0D8C8",
            "text": "#D8D0C0"
        },
        "description": "Contemporary dark base with soft muted florals"
    },
    "sage": {
        "name": "Herbalist's Dream (Sage)",
        "shirt": "#9CAF88",
        "design": {
            "skull": "#FFFFF0",
            "flowers": "#9370DB",
            "accent": "#556B2F",
            "moon": "#F5F5DC",
            "text": "#2F4F2F"
        },
        "description": "Botanical green with mystic purple accents"
    },
    "mauve": {
        "name": "Twilight Bloom (Dusty Rose)",
        "shirt": "#B5838D",
        "design": {
            "skull": "#FFF5EE",
            "flowers": "#8B7D8B",
            "accent": "#7A8A6E",
            "moon": "#FFF0F5",
            "text": "#4A4A4A"
        },
        "description": "Soft romantic mauve with moody undertones"
    },
    "navy": {
        "name": "Midnight Bloom (Navy)",
        "shirt": "#1B2838",
        "design": {
            "skull": "#FFF8DC",
            "flowers": "#D8BFD8",
            "accent": "#A4C2A5",
            "moon": "#E8E0D0",
            "text": "#D0C8B8"
        },
        "description": "Deep navy with luminous pale florals"
    }
}

# Generate mockups for each color combination
for color_key, color_config in color_combinations.items():
    # Front view
    front_svg = create_tshirt_template(color_config['shirt'], color_config['name'])
    front_svg = front_svg.replace('</svg>',
                                  create_memento_mori_variant(color_config['design'], is_back=False) + '\n</svg>')

    with open(f"designs/mockups/memento_mori_{color_key}_front.svg", "w") as f:
        f.write(front_svg)

    # Back view
    back_svg = create_tshirt_template(color_config['shirt'], color_config['name'])
    back_svg = back_svg.replace('</svg>',
                                create_memento_mori_variant(color_config['design'], is_back=True) + '\n</svg>')

    with open(f"designs/mockups/memento_mori_{color_key}_back.svg", "w") as f:
        f.write(back_svg)

# Create HTML viewer for all mockups
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memento Mori Garden - T-Shirt Mockups</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', serif;
            background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
            color: #e8e8e8;
            padding: 40px 20px;
            line-height: 1.6;
        }

        header {
            text-align: center;
            margin-bottom: 50px;
            border-bottom: 2px solid #8B5A8B;
            padding-bottom: 30px;
        }

        h1 {
            font-size: 3em;
            color: #C8A2C8;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }

        .subtitle {
            font-size: 1.2em;
            color: #9CAF88;
            font-style: italic;
        }

        .intro {
            max-width: 900px;
            margin: 0 auto 50px;
            padding: 30px;
            background: rgba(44, 53, 57, 0.6);
            border-radius: 10px;
            border-left: 4px solid #8B5A8B;
        }

        .color-section {
            max-width: 1400px;
            margin: 0 auto 60px;
            padding: 30px;
            background: rgba(44, 53, 57, 0.4);
            border-radius: 15px;
            border: 1px solid rgba(200, 162, 200, 0.3);
        }

        .color-header {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid rgba(200, 162, 200, 0.3);
        }

        .color-swatch {
            width: 60px;
            height: 60px;
            border-radius: 10px;
            margin-right: 20px;
            border: 3px solid #fff;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }

        .color-info h2 {
            color: #C8A2C8;
            font-size: 1.8em;
            margin-bottom: 5px;
        }

        .color-description {
            color: #9CAF88;
            font-style: italic;
        }

        .mockup-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 20px;
        }

        .mockup-card {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .mockup-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(200, 162, 200, 0.3);
        }

        .mockup-card h3 {
            color: #D4C4A8;
            margin-bottom: 15px;
            font-size: 1.3em;
        }

        .mockup-card img {
            width: 100%;
            max-width: 500px;
            border-radius: 8px;
            background: white;
        }

        .specs {
            margin-top: 40px;
            padding: 30px;
            background: rgba(139, 90, 139, 0.2);
            border-radius: 10px;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }

        .specs h2 {
            color: #C8A2C8;
            margin-bottom: 20px;
            font-size: 2em;
        }

        .specs ul {
            list-style: none;
            padding-left: 0;
        }

        .specs li {
            padding: 10px 0;
            border-bottom: 1px solid rgba(200, 162, 200, 0.2);
        }

        .specs li:before {
            content: "✦ ";
            color: #9CAF88;
            font-weight: bold;
            margin-right: 10px;
        }

        .pricing {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }

        .price-card {
            background: rgba(44, 53, 57, 0.6);
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #9CAF88;
        }

        .price-card h3 {
            color: #C8A2C8;
            margin-bottom: 10px;
        }

        .price {
            font-size: 2em;
            color: #9CAF88;
            font-weight: bold;
        }

        @media (max-width: 768px) {
            .mockup-container {
                grid-template-columns: 1fr;
            }

            h1 {
                font-size: 2em;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>🌙 Memento Mori Garden 🌙</h1>
        <p class="subtitle">T-Shirt Color Combinations & Mockups</p>
    </header>

    <div class="intro">
        <p><strong>Design Concept:</strong> A hauntingly beautiful side-profile skull serves as a planter for wildflowers, embodying the phrase "from death, life blooms." This design blends anatomical accuracy with soft botanical elements, creating the perfect balance of gothic and cottage core aesthetics.</p>
        <br>
        <p><strong>Print Placement:</strong> Front print (chest) at standard size, Back print (center back) at premium large size for maximum impact.</p>
    </div>
'''

# Add each color combination section
for color_key, color_config in color_combinations.items():
    html_content += f'''
    <div class="color-section">
        <div class="color-header">
            <div class="color-swatch" style="background-color: {color_config['shirt']};"></div>
            <div class="color-info">
                <h2>{color_config['name']}</h2>
                <p class="color-description">{color_config['description']}</p>
            </div>
        </div>

        <div class="mockup-container">
            <div class="mockup-card">
                <h3>Front View</h3>
                <img src="memento_mori_{color_key}_front.svg" alt="{color_config['name']} - Front">
            </div>
            <div class="mockup-card">
                <h3>Back View</h3>
                <img src="memento_mori_{color_key}_back.svg" alt="{color_config['name']} - Back">
            </div>
        </div>
    </div>
'''

html_content += '''
    <div class="specs">
        <h2>🎨 Design Specifications</h2>
        <ul>
            <li><strong>Design Type:</strong> Front & Back Print (Premium)</li>
            <li><strong>Front Print Size:</strong> 10" x 12" (standard chest placement)</li>
            <li><strong>Back Print Size:</strong> 12" x 14" (large center back placement)</li>
            <li><strong>Colors per Design:</strong> 5-6 colors (multi-color print)</li>
            <li><strong>Recommended Print Method:</strong> Direct-to-Garment (DTG) for detail retention</li>
            <li><strong>File Format:</strong> SVG (scalable vector) - production ready</li>
            <li><strong>Target Audience:</strong> Gothic cottage core enthusiasts, botanical art lovers, memento mori collectors</li>
        </ul>

        <h2 style="margin-top: 40px;">💰 Pricing Strategy</h2>
        <div class="pricing">
            <div class="price-card">
                <h3>Standard Colors</h3>
                <p class="price">$36-38</p>
                <p style="margin-top: 10px; color: #ccc;">Black, Charcoal, Navy</p>
            </div>
            <div class="price-card">
                <h3>Premium Colors</h3>
                <p class="price">$38-40</p>
                <p style="margin-top: 10px; color: #ccc;">Burgundy, Forest, Mauve</p>
            </div>
            <div class="price-card">
                <h3>Specialty Colors</h3>
                <p class="price">$40-42</p>
                <p style="margin-top: 10px; color: #ccc;">Natural, Sage</p>
            </div>
        </div>

        <h2 style="margin-top: 40px;">⭐ Top Recommendations</h2>
        <ul>
            <li><strong>Best Seller Prediction:</strong> Midnight Garden (Black) - Classic goth appeal</li>
            <li><strong>Highest Margin:</strong> Bone Garden (Natural) - Cottage core demographic willing to pay premium</li>
            <li><strong>Most Unique:</strong> Gothic Romance (Burgundy) - Differentiates from competitors</li>
            <li><strong>Seasonal Launch:</strong> Start with Black, Forest, and Burgundy for fall/winter</li>
            <li><strong>Spring Addition:</strong> Add Sage, Natural, and Mauve for cottage core season</li>
        </ul>
    </div>
</body>
</html>
'''

with open("designs/mockups/memento_mori_mockups.html", "w") as f:
    f.write(html_content)

print("✓ Memento Mori Garden mockups created!")
print(f"\n📁 Generated {len(color_combinations) * 2} mockup files:")
print("   - 8 color variations")
print("   - Front and back views for each")
print("\n🎨 Color combinations:")
for color_key, config in color_combinations.items():
    print(f"   - {config['name']}")

print("\n👕 T-shirt colors:")
print("   • Black (Midnight Garden)")
print("   • Natural/Cream (Bone Garden)")
print("   • Forest Green (Woodland Memento)")
print("   • Burgundy (Gothic Romance)")
print("   • Charcoal (Modern Memento)")
print("   • Sage (Herbalist's Dream)")
print("   • Dusty Rose/Mauve (Twilight Bloom)")
print("   • Navy (Midnight Bloom)")

print("\n🌐 View all mockups:")
print("   Open: designs/mockups/memento_mori_mockups.html")

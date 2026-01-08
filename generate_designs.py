#!/usr/bin/env python3
"""
Generate visual SVG mockups for Cottage Core Goth t-shirt designs

Creates SVG files that can be viewed in any browser or converted to PNG.
"""

import os

def create_death_cap_tea_party():
    """Variant 1: Death Cap Tea Party"""
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 500" width="400" height="500">
  <defs>
    <style>
      .vintage-text { font-family: 'Georgia', serif; font-size: 12px; font-style: italic; }
      .title-text { font-family: 'Georgia', serif; font-size: 16px; font-weight: bold; }
    </style>
  </defs>

  <!-- Background -->
  <rect width="400" height="500" fill="#F5F5DC"/>

  <!-- Title -->
  <text x="200" y="30" text-anchor="middle" class="title-text" fill="#8B0000">Death Cap Tea Party</text>

  <!-- Ornate teacup outline -->
  <ellipse cx="200" cy="280" rx="70" ry="15" fill="none" stroke="#36454F" stroke-width="2"/>
  <path d="M 130 280 Q 130 320 150 340 L 250 340 Q 270 320 270 280"
        fill="#F5F5DC" stroke="#36454F" stroke-width="2.5"/>

  <!-- Cup details (cracks) -->
  <line x1="160" y1="290" x2="165" y2="320" stroke="#8B0000" stroke-width="1" opacity="0.5"/>
  <line x1="210" y1="285" x2="215" y2="315" stroke="#8B0000" stroke-width="1" opacity="0.5"/>

  <!-- Gold rim accent -->
  <ellipse cx="200" cy="280" rx="68" ry="13" fill="none" stroke="#DAA520" stroke-width="1.5"/>

  <!-- Teacup handle -->
  <path d="M 270 290 Q 295 290 295 310 Q 295 330 270 330"
        fill="none" stroke="#36454F" stroke-width="2.5"/>

  <!-- Amanita muscaria mushroom growing through cup -->
  <!-- Stem -->
  <rect x="190" y="260" width="20" height="60" fill="#F5F5DC" stroke="#4A5D23" stroke-width="1"/>

  <!-- Cap -->
  <ellipse cx="200" cy="230" rx="45" ry="25" fill="#8B0000"/>
  <ellipse cx="200" cy="230" rx="45" ry="20" fill="#A52A2A"/>

  <!-- White spots on mushroom -->
  <circle cx="185" cy="225" r="4" fill="#F5F5DC"/>
  <circle cx="200" cy="220" r="5" fill="#F5F5DC"/>
  <circle cx="215" cy="225" r="4" fill="#F5F5DC"/>
  <circle cx="195" cy="235" r="3" fill="#F5F5DC"/>
  <circle cx="210" cy="232" r="3" fill="#F5F5DC"/>

  <!-- Deadly nightshade flowers -->
  <circle cx="150" cy="350" r="6" fill="#4A148C"/>
  <circle cx="158" cy="348" r="5" fill="#6A1B9A"/>
  <circle cx="145" cy="355" r="4" fill="#4A148C"/>

  <circle cx="250" cy="350" r="6" fill="#4A148C"/>
  <circle cx="242" cy="348" r="5" fill="#6A1B9A"/>
  <circle cx="255" cy="355" r="4" fill="#4A148C"/>

  <!-- Death's head moth on cup rim -->
  <ellipse cx="230" cy="275" rx="12" ry="8" fill="#8B4513"/>
  <ellipse cx="227" cy="275" rx="5" ry="4" fill="#D2691E"/>
  <ellipse cx="233" cy="275" rx="5" ry="4" fill="#D2691E"/>

  <!-- Moth skull pattern -->
  <circle cx="230" cy="275" r="2" fill="#F5F5DC"/>

  <!-- Wispy steam -->
  <path d="M 200 260 Q 190 240 195 220 Q 200 200 195 180"
        fill="none" stroke="#D3D3D3" stroke-width="1.5" opacity="0.6"/>
  <path d="M 205 260 Q 210 235 208 215 Q 205 195 210 175"
        fill="none" stroke="#D3D3D3" stroke-width="1.5" opacity="0.6"/>

  <!-- Border flowers (simplified) -->
  <!-- Foxglove (left) -->
  <circle cx="50" cy="200" r="4" fill="#C71585"/>
  <circle cx="50" cy="210" r="4" fill="#C71585"/>
  <circle cx="50" cy="220" r="4" fill="#C71585"/>
  <line x1="50" y1="195" x2="50" y2="225" stroke="#4A5D23" stroke-width="2"/>

  <!-- Belladonna (right) -->
  <circle cx="350" cy="200" r="4" fill="#4A148C"/>
  <circle cx="350" cy="210" r="4" fill="#4A148C"/>
  <circle cx="350" cy="220" r="4" fill="#4A148C"/>
  <line x1="350" y1="195" x2="350" y2="225" stroke="#4A5D23" stroke-width="2"/>

  <!-- Quote at bottom -->
  <text x="200" y="420" text-anchor="middle" class="vintage-text" fill="#36454F">
    "Some things are beautiful because they're deadly"
  </text>

  <!-- Decorative corners -->
  <path d="M 20 20 L 20 60 M 20 20 L 60 20" stroke="#8B0000" stroke-width="1.5" fill="none"/>
  <path d="M 380 20 L 380 60 M 380 20 L 340 20" stroke="#8B0000" stroke-width="1.5" fill="none"/>
  <path d="M 20 480 L 20 440 M 20 480 L 60 480" stroke="#8B0000" stroke-width="1.5" fill="none"/>
  <path d="M 380 480 L 380 440 M 380 480 L 340 480" stroke="#8B0000" stroke-width="1.5" fill="none"/>
</svg>'''

    with open('/home/user/the-office/designs/death_cap_tea_party.svg', 'w') as f:
        f.write(svg)
    print("✓ Created: death_cap_tea_party.svg")


def create_memento_mori_garden():
    """Variant 2: Memento Mori Garden"""
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 500" width="400" height="500">
  <defs>
    <style>
      .script-text { font-family: 'Brush Script MT', cursive; font-size: 14px; }
      .title-text { font-family: 'Georgia', serif; font-size: 16px; font-weight: bold; }
    </style>
  </defs>

  <!-- Background (would be black t-shirt) -->
  <rect width="400" height="500" fill="#1a1a1a"/>

  <!-- Title -->
  <text x="200" y="30" text-anchor="middle" class="title-text" fill="#C8A2C8">Memento Mori Garden</text>

  <!-- Moon phases above skull -->
  <circle cx="140" cy="80" r="8" fill="none" stroke="#FFF8DC" stroke-width="1.5"/>
  <circle cx="140" cy="80" r="8" fill="#FFF8DC" clip-path="inset(0 50% 0 0)"/>

  <circle cx="200" cy="70" r="12" fill="#FFF8DC"/>

  <circle cx="260" cy="80" r="8" fill="none" stroke="#FFF8DC" stroke-width="1.5"/>
  <circle cx="260" cy="80" r="8" fill="#FFF8DC" clip-path="inset(0 0 0 50%)"/>

  <!-- Skull (side profile) -->
  <!-- Cranium -->
  <ellipse cx="200" cy="200" rx="60" ry="70" fill="#FFF8DC" stroke="#2C3539" stroke-width="2"/>

  <!-- Eye socket -->
  <ellipse cx="230" cy="185" rx="18" ry="22" fill="#2C3539"/>

  <!-- Nasal cavity -->
  <path d="M 245 210 L 255 215 L 245 220 Z" fill="#2C3539"/>

  <!-- Jaw line -->
  <path d="M 180 230 Q 220 250 260 240" fill="none" stroke="#2C3539" stroke-width="2"/>

  <!-- Teeth (simplified) -->
  <rect x="230" y="238" width="6" height="8" fill="#FFF8DC" stroke="#2C3539" stroke-width="0.5"/>
  <rect x="237" y="238" width="6" height="8" fill="#FFF8DC" stroke="#2C3539" stroke-width="0.5"/>
  <rect x="244" y="238" width="6" height="8" fill="#FFF8DC" stroke="#2C3539" stroke-width="0.5"/>

  <!-- Flowers growing from skull -->
  <!-- Lavender sprigs -->
  <line x1="190" y1="140" x2="185" y2="100" stroke="#9CAF88" stroke-width="2"/>
  <circle cx="185" cy="95" r="3" fill="#C8A2C8"/>
  <circle cx="187" cy="100" r="3" fill="#C8A2C8"/>
  <circle cx="183" cy="105" r="3" fill="#C8A2C8"/>
  <circle cx="188" cy="110" r="3" fill="#C8A2C8"/>

  <line x1="210" y1="140" x2="205" y2="95" stroke="#9CAF88" stroke-width="2"/>
  <circle cx="205" cy="90" r="3" fill="#C8A2C8"/>
  <circle cx="207" cy="95" r="3" fill="#C8A2C8"/>
  <circle cx="203" cy="100" r="3" fill="#C8A2C8"/>
  <circle cx="206" cy="105" r="3" fill="#C8A2C8"/>

  <!-- Roses from eye socket -->
  <line x1="230" y1="185" x2="240" y2="150" stroke="#9CAF88" stroke-width="1.5"/>
  <circle cx="240" cy="145" r="8" fill="#DCAE96"/>
  <circle cx="238" cy="145" r="5" fill="#D4A5A5"/>
  <circle cx="242" cy="145" r="5" fill="#D4A5A5"/>

  <line x1="235" y1="185" x2="250" y2="155" stroke="#9CAF88" stroke-width="1.5"/>
  <circle cx="250" cy="150" r="7" fill="#DCAE96"/>
  <circle cx="248" cy="150" r="4" fill="#D4A5A5"/>

  <!-- Forget-me-nots -->
  <circle cx="175" cy="165" r="4" fill="#87CEEB"/>
  <circle cx="173" cy="165" r="1.5" fill="#FFD700"/>
  <circle cx="180" cy="170" r="4" fill="#87CEEB"/>
  <circle cx="178" cy="170" r="1.5" fill="#FFD700"/>
  <circle cx="172" cy="172" r="4" fill="#87CEEB"/>
  <circle cx="170" cy="172" r="1.5" fill="#FFD700"/>

  <!-- Baby's breath (small clusters) -->
  <circle cx="160" cy="180" r="2" fill="#FFF8DC"/>
  <circle cx="165" cy="182" r="2" fill="#FFF8DC"/>
  <circle cx="163" cy="177" r="2" fill="#FFF8DC"/>
  <circle cx="168" cy="180" r="2" fill="#FFF8DC"/>

  <!-- Mushrooms at base -->
  <ellipse cx="180" cy="270" rx="8" ry="5" fill="#D4A5A5"/>
  <rect x="176" y="265" width="8" height="10" fill="#FFF8DC" stroke="#9CAF88" stroke-width="0.5"/>

  <ellipse cx="220" cy="275" rx="6" ry="4" fill="#D4A5A5"/>
  <rect x="217" y="271" width="6" height="8" fill="#FFF8DC" stroke="#9CAF88" stroke-width="0.5"/>

  <!-- Small snail on cheek -->
  <ellipse cx="210" cy="210" rx="6" ry="4" fill="#8B7355"/>
  <circle cx="208" cy="210" r="3" fill="#D2B48C"/>
  <line x1="207" y1="208" x2="206" y2="206" stroke="#2C3539" stroke-width="0.5"/>
  <line x1="209" y1="208" x2="210" y2="206" stroke="#2C3539" stroke-width="0.5"/>

  <!-- Roots at bottom -->
  <path d="M 200 280 Q 190 320 185 350" stroke="#9CAF88" stroke-width="1.5" fill="none"/>
  <path d="M 200 280 Q 210 320 215 350" stroke="#9CAF88" stroke-width="1.5" fill="none"/>
  <path d="M 200 280 Q 200 315 200 350" stroke="#9CAF88" stroke-width="1.5" fill="none"/>

  <!-- Quote at bottom -->
  <text x="200" y="430" text-anchor="middle" class="script-text" fill="#C8A2C8">
    From death, life blooms
  </text>
</svg>'''

    with open('/home/user/the-office/designs/memento_mori_garden.svg', 'w') as f:
        f.write(svg)
    print("✓ Created: memento_mori_garden.svg")


def create_feral_familiar():
    """Variant 3: Feral Familiar"""
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 500" width="400" height="500">
  <defs>
    <style>
      .bold-text { font-family: 'Impact', sans-serif; font-size: 24px; font-weight: bold; letter-spacing: 2px; }
      .title-text { font-family: 'Georgia', serif; font-size: 16px; font-weight: bold; }
    </style>
  </defs>

  <!-- Background (black t-shirt) -->
  <rect width="400" height="500" fill="#2a2a2a"/>

  <!-- Title -->
  <text x="200" y="30" text-anchor="middle" class="title-text" fill="#FFFFF0">Feral Familiar</text>

  <!-- Circular moon border -->
  <circle cx="200" cy="250" r="130" fill="none" stroke="#FFFFF0" stroke-width="1.5" stroke-dasharray="5,5"/>

  <!-- Moon phases around circle -->
  <circle cx="200" cy="110" r="6" fill="#FFFFF0"/>
  <circle cx="280" cy="165" r="5" fill="none" stroke="#FFFFF0" stroke-width="1"/>
  <circle cx="280" cy="165" r="5" fill="#FFFFF0" clip-path="inset(0 50% 0 0)"/>
  <circle cx="280" cy="335" r="5" fill="none" stroke="#FFFFF0" stroke-width="1"/>
  <circle cx="280" cy="335" r="5" fill="#FFFFF0" clip-path="inset(0 0 0 50%)"/>
  <circle cx="120" cy="165" r="4" fill="none" stroke="#FFFFF0" stroke-width="1"/>
  <circle cx="120" cy="335" r="4" fill="none" stroke="#FFFFF0" stroke-width="1"/>

  <!-- Stars -->
  <text x="150" y="140" font-size="12" fill="#FFFFF0">✦</text>
  <text x="250" y="140" font-size="12" fill="#FFFFF0">✦</text>
  <text x="140" y="360" font-size="10" fill="#FFFFF0">✦</text>
  <text x="260" y="360" font-size="10" fill="#FFFFF0">✦</text>
  <text x="90" y="250" font-size="8" fill="#FFFFF0">✦</text>
  <text x="310" y="250" font-size="8" fill="#FFFFF0">✦</text>

  <!-- Luna moth wings (behind skull) -->
  <!-- Left wing -->
  <ellipse cx="160" cy="240" rx="45" ry="30" fill="#A0522D" opacity="0.8"/>
  <ellipse cx="160" cy="240" rx="35" ry="22" fill="#D2691E" opacity="0.6"/>
  <circle cx="155" cy="235" r="6" fill="#FFFFF0" opacity="0.9"/>
  <circle cx="155" cy="235" r="3" fill="#2a2a2a"/>

  <!-- Right wing -->
  <ellipse cx="240" cy="240" rx="45" ry="30" fill="#A0522D" opacity="0.8"/>
  <ellipse cx="240" cy="240" rx="35" ry="22" fill="#D2691E" opacity="0.6"/>
  <circle cx="245" cy="235" r="6" fill="#FFFFF0" opacity="0.9"/>
  <circle cx="245" cy="235" r="3" fill="#2a2a2a"/>

  <!-- Cat skull (front-facing) -->
  <!-- Main cranium -->
  <ellipse cx="200" cy="230" rx="40" ry="45" fill="#FFFFF0"/>

  <!-- Eye sockets -->
  <ellipse cx="185" cy="220" rx="12" ry="15" fill="#2a2a2a"/>
  <ellipse cx="215" cy="220" rx="12" ry="15" fill="#2a2a2a"/>

  <!-- Nasal cavity (cat nose shape) -->
  <path d="M 195 240 L 200 245 L 205 240 L 200 238 Z" fill="#2a2a2a"/>

  <!-- Cheekbones -->
  <ellipse cx="170" cy="235" rx="8" ry="12" fill="#FFFFF0" opacity="0.3"/>
  <ellipse cx="230" cy="235" rx="8" ry="12" fill="#FFFFF0" opacity="0.3"/>

  <!-- Upper jaw/teeth -->
  <path d="M 175 250 Q 200 258 225 250" stroke="#2a2a2a" stroke-width="1.5" fill="none"/>

  <!-- Fangs -->
  <rect x="188" y="250" width="4" height="12" fill="#FFFFF0" stroke="#2a2a2a" stroke-width="0.5"/>
  <rect x="208" y="250" width="4" height="12" fill="#FFFFF0" stroke="#2a2a2a" stroke-width="0.5"/>

  <!-- Wildflower crown -->
  <line x1="160" y1="195" x2="240" y2="195" stroke="#2C5530" stroke-width="2"/>

  <!-- Flowers in crown -->
  <circle cx="170" cy="188" r="6" fill="#FFD700"/>
  <circle cx="168" cy="188" r="2" fill="#8B4513"/>

  <circle cx="185" cy="185" r="5" fill="#E6E6FA"/>
  <circle cx="183" cy="185" r="1.5" fill="#FFD700"/>

  <circle cx="200" cy="183" r="7" fill="#FFC0CB"/>
  <circle cx="198" cy="183" r="3" fill="#FF69B4"/>

  <circle cx="215" cy="185" r="5" fill="#E6E6FA"/>
  <circle cx="213" cy="185" r="1.5" fill="#FFD700"/>

  <circle cx="230" cy="188" r="6" fill="#FFD700"/>
  <circle cx="228" cy="188" r="2" fill="#8B4513"/>

  <!-- Thorns in crown -->
  <path d="M 175 195 L 173 200" stroke="#2C5530" stroke-width="1.5"/>
  <path d="M 190 195 L 188 200" stroke="#2C5530" stroke-width="1.5"/>
  <path d="M 210 195 L 208 200" stroke="#2C5530" stroke-width="1.5"/>
  <path d="M 225 195 L 223 200" stroke="#2C5530" stroke-width="1.5"/>

  <!-- Hands reaching up from bottom -->
  <!-- Left hand -->
  <path d="M 140 380 L 145 355 L 150 350 L 155 345" stroke="#FFFFF0" stroke-width="2" fill="none"/>
  <path d="M 145 355 L 148 348" stroke="#FFFFF0" stroke-width="1.5" fill="none"/>
  <path d="M 145 355 L 142 348" stroke="#FFFFF0" stroke-width="1.5" fill="none"/>

  <!-- Right hand -->
  <path d="M 260 380 L 255 355 L 250 350 L 245 345" stroke="#FFFFF0" stroke-width="2" fill="none"/>
  <path d="M 255 355 L 252 348" stroke="#FFFFF0" stroke-width="1.5" fill="none"/>
  <path d="M 255 355 L 258 348" stroke="#FFFFF0" stroke-width="1.5" fill="none"/>

  <!-- Herbs in hands -->
  <line x1="155" y1="345" x2="158" y2="335" stroke="#2C5530" stroke-width="1"/>
  <circle cx="158" cy="332" r="2" fill="#C8A2C8"/>

  <line x1="245" y1="345" x2="242" y2="335" stroke="#2C5530" stroke-width="1"/>
  <circle cx="242" cy="332" r="2" fill="#C8A2C8"/>

  <!-- Mushrooms in hands -->
  <ellipse cx="150" cy="352" rx="5" ry="3" fill="#8B0000"/>
  <rect x="147" y="350" width="6" height="6" fill="#FFFFF0" stroke="#2C5530" stroke-width="0.5"/>

  <ellipse cx="250" cy="352" rx="5" ry="3" fill="#8B0000"/>
  <rect x="247" y="350" width="6" height="6" fill="#FFFFF0" stroke="#2C5530" stroke-width="0.5"/>

  <!-- Text at bottom -->
  <text x="200" y="440" text-anchor="middle" class="bold-text" fill="#FFFFF0">
    FAMILIAR
  </text>
</svg>'''

    with open('/home/user/the-office/designs/feral_familiar.svg', 'w') as f:
        f.write(svg)
    print("✓ Created: feral_familiar.svg")


def create_ouija_garden():
    """Variant 4: Ouija in the Garden"""
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 600" width="400" height="600">
  <defs>
    <style>
      .ouija-text { font-family: 'Courier New', monospace; font-size: 16px; font-weight: bold; }
      .ouija-letters { font-family: 'Georgia', serif; font-size: 24px; font-weight: bold; }
      .title-text { font-family: 'Georgia', serif; font-size: 16px; font-weight: bold; }
      .script-text { font-family: 'Brush Script MT', cursive; font-size: 12px; }
    </style>

    <!-- Wood grain pattern -->
    <pattern id="wood" x="0" y="0" width="100" height="100" patternUnits="userSpaceOnUse">
      <rect width="100" height="100" fill="#F4E8C1"/>
      <path d="M 0 20 Q 50 25 100 20" stroke="#D4C4A1" stroke-width="0.5" fill="none" opacity="0.3"/>
      <path d="M 0 40 Q 50 45 100 40" stroke="#D4C4A1" stroke-width="0.5" fill="none" opacity="0.3"/>
      <path d="M 0 60 Q 50 55 100 60" stroke="#D4C4A1" stroke-width="0.5" fill="none" opacity="0.3"/>
      <path d="M 0 80 Q 50 85 100 80" stroke="#D4C4A1" stroke-width="0.5" fill="none" opacity="0.3"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="400" height="600" fill="#2a2a2a"/>

  <!-- Title -->
  <text x="200" y="30" text-anchor="middle" class="title-text" fill="#F4E8C1">Ouija in the Garden</text>

  <!-- Main Ouija board -->
  <rect x="50" y="70" width="300" height="440" rx="15" fill="url(#wood)" stroke="#1C1C1C" stroke-width="3"/>

  <!-- Decorative corners -->
  <circle cx="70" cy="90" r="8" fill="none" stroke="#1C1C1C" stroke-width="1.5"/>
  <circle cx="330" cy="90" r="8" fill="none" stroke="#1C1C1C" stroke-width="1.5"/>
  <circle cx="70" cy="490" r="8" fill="none" stroke="#1C1C1C" stroke-width="1.5"/>
  <circle cx="330" cy="490" r="8" fill="none" stroke="#1C1C1C" stroke-width="1.5"/>

  <!-- Crescent moon at top -->
  <circle cx="200" cy="120" r="20" fill="none" stroke="#1C1C1C" stroke-width="2"/>
  <circle cx="205" cy="120" r="20" fill="#F4E8C1"/>

  <!-- YES and NO -->
  <text x="120" y="175" class="ouija-text" fill="#1C1C1C">YES</text>
  <text x="260" y="175" class="ouija-text" fill="#1C1C1C">NO</text>

  <!-- Vines growing through YES -->
  <path d="M 115 168 Q 125 165 135 168" stroke="#A8B5A0" stroke-width="2" fill="none"/>
  <circle cx="125" cy="162" r="4" fill="#D4A5A5"/>

  <!-- Vines growing through NO -->
  <path d="M 255 168 Q 270 165 285 168" stroke="#A8B5A0" stroke-width="2" fill="none"/>
  <circle cx="270" cy="162" r="4" fill="#D4A5A5"/>

  <!-- Alphabet arc -->
  <text x="90" y="230" class="ouija-letters" fill="#1C1C1C">A</text>
  <text x="115" y="220" class="ouija-letters" fill="#1C1C1C">B</text>
  <text x="140" y="215" class="ouija-letters" fill="#1C1C1C">C</text>
  <text x="165" y="212" class="ouija-letters" fill="#1C1C1C">D</text>
  <text x="190" y="210" class="ouija-letters" fill="#1C1C1C">E</text>
  <text x="215" y="212" class="ouija-letters" fill="#1C1C1C">F</text>
  <text x="240" y="215" class="ouija-letters" fill="#1C1C1C">G</text>
  <text x="265" y="220" class="ouija-letters" fill="#1C1C1C">H</text>
  <text x="290" y="230" class="ouija-letters" fill="#1C1C1C">I</text>

  <!-- Ivy wrapping around letters -->
  <path d="M 85 235 Q 100 230 120 230 Q 150 230 180 230 Q 210 230 240 230 Q 270 230 300 235"
        stroke="#A8B5A0" stroke-width="1.5" fill="none"/>
  <circle cx="130" cy="228" r="3" fill="#A8B5A0"/>
  <circle cx="200" cy="228" r="3" fill="#A8B5A0"/>
  <circle cx="270" cy="228" r="3" fill="#A8B5A0"/>

  <!-- Second row of alphabet -->
  <text x="95" y="280" class="ouija-letters" fill="#1C1C1C">J</text>
  <text x="120" y="275" class="ouija-letters" fill="#1C1C1C">K</text>
  <text x="145" y="272" class="ouija-letters" fill="#1C1C1C">L</text>
  <text x="170" y="270" class="ouija-letters" fill="#1C1C1C">M</text>
  <text x="195" y="270" class="ouija-letters" fill="#1C1C1C">N</text>
  <text x="220" y="272" class="ouija-letters" fill="#1C1C1C">O</text>
  <text x="245" y="275" class="ouija-letters" fill="#1C1C1C">P</text>
  <text x="270" y="280" class="ouija-letters" fill="#1C1C1C">Q</text>

  <!-- Third row of alphabet -->
  <text x="100" y="330" class="ouija-letters" fill="#1C1C1C">R</text>
  <text x="130" y="325" class="ouija-letters" fill="#1C1C1C">S</text>
  <text x="160" y="322" class="ouija-letters" fill="#1C1C1C">T</text>
  <text x="190" y="320" class="ouija-letters" fill="#1C1C1C">U</text>
  <text x="220" y="322" class="ouija-letters" fill="#1C1C1C">V</text>
  <text x="250" y="325" class="ouija-letters" fill="#1C1C1C">W</text>
  <text x="280" y="330" class="ouija-letters" fill="#1C1C1C">X</text>

  <!-- Flowers blooming from U -->
  <line x1="205" y1="315" x2="210" y2="300" stroke="#A8B5A0" stroke-width="1"/>
  <circle cx="210" cy="297" r="4" fill="#C8A2C8"/>

  <!-- Fourth row -->
  <text x="140" y="375" class="ouija-letters" fill="#1C1C1C">Y</text>
  <text x="230" y="375" class="ouija-letters" fill="#1C1C1C">Z</text>

  <!-- Mushrooms growing from corners -->
  <ellipse cx="85" cy="485" rx="8" ry="5" fill="#8B0000"/>
  <rect x="80" y="480" width="10" height="10" fill="#F4E8C1" stroke="#A8B5A0" stroke-width="0.5"/>
  <circle cx="83" cy="483" r="2" fill="#F5F5DC"/>
  <circle cx="88" cy="481" r="2" fill="#F5F5DC"/>

  <ellipse cx="315" cy="485" rx="8" ry="5" fill="#8B0000"/>
  <rect x="310" y="480" width="10" height="10" fill="#F4E8C1" stroke="#A8B5A0" stroke-width="0.5"/>
  <circle cx="313" cy="483" r="2" fill="#F5F5DC"/>
  <circle cx="318" cy="481" r="2" fill="#F5F5DC"/>

  <!-- Numbers -->
  <text x="110" y="420" class="ouija-letters" fill="#1C1C1C">1 2 3 4 5 6 7 8 9 0</text>

  <!-- Moth planchette in center -->
  <ellipse cx="200" cy="350" rx="30" ry="20" fill="#8B4513" stroke="#1C1C1C" stroke-width="2"/>

  <!-- Moth wings -->
  <ellipse cx="185" cy="350" rx="15" ry="12" fill="#D2691E" opacity="0.7"/>
  <ellipse cx="215" cy="350" rx="15" ry="12" fill="#D2691E" opacity="0.7"/>

  <!-- Moth skull pattern -->
  <circle cx="200" cy="350" r="6" fill="#F4E8C1"/>
  <circle cx="197" cy="348" r="1.5" fill="#1C1C1C"/>
  <circle cx="203" cy="348" r="1.5" fill="#1C1C1C"/>

  <!-- Planchette pointer -->
  <circle cx="200" cy="350" r="8" fill="none" stroke="#F4E8C1" stroke-width="1.5"/>
  <circle cx="200" cy="350" r="3" fill="none" stroke="#F4E8C1" stroke-width="1"/>

  <!-- GOODBYE at bottom -->
  <text x="200" y="470" text-anchor="middle" class="ouija-text" fill="#1C1C1C">GOODBYE</text>

  <!-- Thorny vines wrapping around GOODBYE -->
  <path d="M 140 465 Q 160 463 180 465 Q 200 467 220 465 Q 240 463 260 465"
        stroke="#A8B5A0" stroke-width="1.5" fill="none"/>
  <path d="M 155 465 L 153 460" stroke="#A8B5A0" stroke-width="1"/>
  <path d="M 185 465 L 183 460" stroke="#A8B5A0" stroke-width="1"/>
  <path d="M 215 465 L 213 460" stroke="#A8B5A0" stroke-width="1"/>
  <path d="M 245 465 L 243 460" stroke="#A8B5A0" stroke-width="1"/>

  <!-- Roses on thorns -->
  <circle cx="170" cy="463" r="4" fill="#D4A5A5"/>
  <circle cx="230" cy="463" r="4" fill="#D4A5A5"/>

  <!-- Quote at bottom -->
  <text x="200" y="550" text-anchor="middle" class="script-text" fill="#F4E8C1">
    "Ask the garden what grows in darkness"
  </text>

  <!-- Spider web in corner (decorative) -->
  <path d="M 330 90 L 345 95 M 330 90 L 335 105 M 330 90 L 342 105"
        stroke="#D3D3D3" stroke-width="0.5" opacity="0.5"/>
</svg>'''

    with open('/home/user/the-office/designs/ouija_garden.svg', 'w') as f:
        f.write(svg)
    print("✓ Created: ouija_garden.svg")


def main():
    # Create designs directory
    os.makedirs('/home/user/the-office/designs', exist_ok=True)

    print("=" * 80)
    print("GENERATING COTTAGE CORE GOTH DESIGN MOCKUPS")
    print("=" * 80)
    print()

    print("Creating SVG design files...")
    print()

    create_death_cap_tea_party()
    create_memento_mori_garden()
    create_feral_familiar()
    create_ouija_garden()

    print()
    print("=" * 80)
    print("✓ All designs created!")
    print()
    print("View the designs by opening the SVG files in a web browser:")
    print("  - designs/death_cap_tea_party.svg")
    print("  - designs/memento_mori_garden.svg")
    print("  - designs/feral_familiar.svg")
    print("  - designs/ouija_garden.svg")
    print()
    print("These SVG files can be:")
    print("  • Viewed in any web browser")
    print("  • Edited in vector graphics software (Inkscape, Illustrator)")
    print("  • Converted to PNG using online tools or imagemagick")
    print("  • Sent directly to print-on-demand services")
    print("=" * 80)


if __name__ == "__main__":
    main()

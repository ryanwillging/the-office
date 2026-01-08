#!/usr/bin/env python3
"""
T-Shirt Business Planning with AI Agents

This script uses the agent suite to:
1. Research current trends (CPO)
2. Design t-shirt concepts (CPO)
3. Plan marketing and sales (CPO)
4. Assess technical/production feasibility (CTO)
5. Create strategic plan (CEO)
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
print("T-SHIRT BUSINESS PLANNING SESSION")
print("=" * 80)
print()

# Initialize business
business = Business()
cpo = business.get_agent("CPO")
cto = business.get_agent("CTO")
ceo = business.get_agent("CEO")

# Step 1: CPO researches current trends
print("STEP 1: Researching Current Trends")
print("-" * 80)
print("CPO is analyzing current internet trends for t-shirt design opportunities...")
print()

trend_research = cpo.think("""
Research and identify the top 3-5 current internet trends that would make great t-shirt designs.

Consider trends from:
- Social media (memes, viral content, cultural moments)
- Pop culture and entertainment
- Technology and AI
- Sustainability and social causes
- Niche communities and subcultures

For each trend, provide:
1. The trend name and description
2. Why it's popular right now
3. Target audience demographics
4. Estimated market size/demand
5. T-shirt design potential (high/medium/low)

Recommend the TOP trend to pursue and explain why.
""")

print(trend_research)
print()
print("=" * 80)
print()

# Step 2: CPO designs t-shirt based on selected trend
print("STEP 2: Designing T-Shirt Concept")
print("-" * 80)
print("CPO is creating t-shirt design concepts...")
print()

design_concept = cpo.think(f"""
Based on the trend research, create a detailed t-shirt design concept.

Previous trend research:
{trend_research}

Provide:
1. Design concept name and tagline
2. Visual design description (colors, graphics, typography, style)
3. Message/theme of the design
4. Multiple variants (e.g., different color schemes, minimal vs detailed versions)
5. Target customer profile
6. Pricing strategy recommendation ($15-$40 range)
7. Why this design will resonate with the target audience

Make the design modern, memorable, and marketable.
""")

print(design_concept)
print()
print("=" * 80)
print()

# Step 3: CTO assesses print-on-demand platforms and technical setup
print("STEP 3: Technical Feasibility & Production Planning")
print("-" * 80)
print("CTO is evaluating print-on-demand platforms and technical infrastructure...")
print()

tech_assessment = cto.think(f"""
Assess the technical feasibility and recommend production approach for this t-shirt business.

T-Shirt Design Concept:
{design_concept}

Provide:
1. Top 3 print-on-demand platforms comparison (Printful, Printify, Teespring, etc.)
   - Pricing structure
   - Quality and options
   - Integration capabilities
   - Pros and cons
2. Recommended platform and why
3. E-commerce platform recommendation (Shopify, WooCommerce, Etsy, etc.)
4. Technical infrastructure needed:
   - Website/storefront setup
   - Payment processing
   - Order automation
   - Inventory management (if any)
5. Design file requirements and preparation
6. Estimated per-unit costs and margins
7. Quality control considerations
8. Implementation roadmap

Focus on minimizing upfront costs and operational complexity.
""")

print(tech_assessment)
print()
print("=" * 80)
print()

# Step 4: CPO creates marketing and sales plan
print("STEP 4: Marketing & Sales Strategy")
print("-" * 80)
print("CPO is developing marketing and sales strategy...")
print()

marketing_plan = cpo.create_marketing_campaign(
    goal="Launch t-shirt line and achieve 100 sales in first month",
    target_audience="Based on the trend research and design concept",
    budget=500  # Starting with modest budget
)

print(f"Goal: {marketing_plan['goal']}")
print(f"Target Audience: {marketing_plan['target_audience']}")
print(f"Budget: ${marketing_plan['budget']}")
print()
print("Campaign Plan:")
print(marketing_plan['campaign'])
print()
print("=" * 80)
print()

# Step 5: Record initial metrics and projections
print("STEP 5: Setting Initial Metrics & Projections")
print("-" * 80)

business.record_metrics({
    'customer': {
        'target_conversion_rate': 0.03,  # 3% visitor to customer
        'target_retention_rate': 0.25,   # 25% repeat purchase rate
        'target_satisfaction': 4.5       # 4.5/5 stars
    },
    'operational': {
        'target_error_rate': 0.01,       # 1% order issues
        'target_fulfillment_time': 7     # 7 days average
    },
    'financial': {
        'target_profit_margin': 0.40,    # 40% margin
        'startup_costs': 500,            # Initial investment
        'target_first_month_revenue': 2000  # 100 sales at ~$20
    }
})

print("Initial metrics and targets set:")
metrics_summary = business.metrics_tracker.get_summary()
for category, metrics in metrics_summary.items():
    if metrics:
        print(f"\n{category.upper()}:")
        for name, value in metrics.items():
            print(f"  {name}: {value}")
print()
print("=" * 80)
print()

# Step 6: CEO creates comprehensive strategic plan
print("STEP 6: CEO Strategic Plan")
print("-" * 80)
print("CEO is synthesizing all inputs into a comprehensive strategic plan...")
print()

strategic_plan = ceo.think(f"""
Create a comprehensive strategic plan for launching this t-shirt business.

You have received input from your team:

CPO TREND RESEARCH:
{trend_research}

CPO DESIGN CONCEPT:
{design_concept}

CTO TECHNICAL ASSESSMENT:
{tech_assessment}

CPO MARKETING PLAN:
{marketing_plan['campaign']}

Create a strategic plan that includes:

1. EXECUTIVE SUMMARY
   - Business concept in 2-3 sentences
   - Key success factors

2. PRODUCT STRATEGY
   - Core product offering
   - Pricing strategy
   - Expansion opportunities

3. GO-TO-MARKET STRATEGY
   - Launch timeline (30/60/90 days)
   - Marketing channels and tactics
   - Customer acquisition approach

4. OPERATIONS PLAN
   - Production and fulfillment approach
   - Technology stack
   - Quality assurance

5. FINANCIAL PROJECTIONS
   - Startup costs breakdown
   - First 3 months revenue/cost projections
   - Break-even analysis
   - Target profit margins

6. KEY METRICS & MILESTONES
   - What we'll measure
   - Month 1, 2, 3 milestones
   - Success criteria

7. RISKS & MITIGATION
   - Top 3 risks
   - How we'll address them

8. NEXT STEPS
   - Immediate actions (Week 1)
   - What needs approval/decision

Make this actionable and realistic for a bootstrapped startup with $500 initial budget.
""")

print(strategic_plan)
print()
print("=" * 80)
print()

# Save the strategic plan to a file
print("SAVING STRATEGIC PLAN")
print("-" * 80)

with open("/home/user/the-office/TSHIRT_STRATEGIC_PLAN.md", "w") as f:
    f.write("# T-Shirt Business Strategic Plan\n\n")
    f.write("*Generated by AI Business Agent Suite*\n\n")
    f.write("---\n\n")

    f.write("## 1. Trend Research (CPO)\n\n")
    f.write(trend_research)
    f.write("\n\n---\n\n")

    f.write("## 2. Design Concept (CPO)\n\n")
    f.write(design_concept)
    f.write("\n\n---\n\n")

    f.write("## 3. Technical Assessment & Production (CTO)\n\n")
    f.write(tech_assessment)
    f.write("\n\n---\n\n")

    f.write("## 4. Marketing & Sales Strategy (CPO)\n\n")
    f.write(f"**Goal:** {marketing_plan['goal']}\n\n")
    f.write(f"**Target Audience:** {marketing_plan['target_audience']}\n\n")
    f.write(f"**Budget:** ${marketing_plan['budget']}\n\n")
    f.write(marketing_plan['campaign'])
    f.write("\n\n---\n\n")

    f.write("## 5. CEO Strategic Plan\n\n")
    f.write(strategic_plan)
    f.write("\n\n---\n\n")

    f.write("## 6. Initial Metrics & Targets\n\n")
    for category, metrics in metrics_summary.items():
        if metrics:
            f.write(f"\n### {category.upper()}\n\n")
            for name, value in metrics.items():
                f.write(f"- **{name}**: {value}\n")

print("✓ Strategic plan saved to: TSHIRT_STRATEGIC_PLAN.md")
print()
print("=" * 80)
print()
print("PLANNING SESSION COMPLETE!")
print()
print("Review the strategic plan in TSHIRT_STRATEGIC_PLAN.md")
print()

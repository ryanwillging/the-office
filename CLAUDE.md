# The Office - AI Business Agent Suite

## Project Overview

An AI-powered business management system featuring autonomous agents (CEO, CPO, CTO) that collaborate to run a small business. Currently operating a "HUMAN-MADE™" premium t-shirt brand.

**Tech Stack**: Python 3.8+, Anthropic Claude API, Shopify, Gemini API (Imagen), Printful POD

## Architecture Quick Reference

```
Business Orchestrator (src/business.py)
       ├── CEO Agent - Strategic decisions, final authority
       ├── CPO Agent - Product, customer, marketing
       └── CTO Agent - Technical, automation, infrastructure
             ├── Message Bus (inter-agent communication)
             └── Metrics Tracker (customer/operational/financial)
```

**Key Files**:
- `src/business.py` - Main orchestrator
- `src/agents/` - Agent implementations (CEO, CPO, CTO inherit from base_agent.py)
- `src/core/messaging.py` - Message bus for agent communication
- `src/core/metrics.py` - Business metrics tracking
- `shopify_setup.py` - Shopify product creation with Gemini image generation

## Business Context

### Brand: HUMAN-MADE™
- **Position**: Premium anti-AI statement apparel for creative professionals
- **Tagline**: "Crafted by Humans, For Humans"
- **Price Point**: $32-42 (premium positioning)
- **Target**: Creative professionals aged 26-38 who value authenticity

### Current Product Line: Cottage Core Goth
- Memento Mori Garden (skull with wildflowers, moon phases)
- Color variants: Black, Cream, Forest, Burgundy, Charcoal, Sage, Mauve, Navy
- Sizes: XS-3XL

### Key Brand Guidelines
- Celebrate human creativity over AI
- Blend gothic aesthetic with cottage core softness
- Quality messaging must match quality product
- Never undermine the "human-made" ethos

## Development Guidelines

### Code Style
- Follow existing patterns in the codebase
- Agents communicate through message bus, not direct method calls
- Record metrics regularly for business insights
- Use typed messages (REQUEST, RESPONSE, NOTIFICATION, DECISION_NEEDED)

### Testing
```bash
python main.py          # Run demo
python examples/*.py    # Run specific examples
```

### Adding New Features
1. New agents: Inherit from `BaseAgent`, implement `get_system_prompt()`
2. New skills: Use `CTO.create_skill()` pattern
3. New metrics: Use category (customer/operational/financial)

## Common Operations

### Shopify Product Management
```bash
python shopify_setup.py  # Create products with Gemini-generated images
```

### Generate T-Shirt Mockups
- Design files in `designs/` directory
- Mockups saved to `generated_images/`

### Agent Interaction Example
```python
from src.business import Business
business = Business()
review = business.review_business()  # CEO strategic review
analysis = business.analyze_customer_feedback(feedback)  # CPO analysis
```

## Environment Variables Required

```
ANTHROPIC_API_KEY=       # Claude API for agent reasoning
SHOPIFY_STORE=           # e.g., store-name.myshopify.com
SHOPIFY_API_KEY=         # Shopify Admin API key
SHOPIFY_API_SECRET=      # Shopify Admin API secret/token
GEMINI_API_KEY=          # Google Gemini API for image generation
```

## Important Directories

- `designs/` - Design specifications and product descriptions
- `docs/` - Architecture and usage documentation
- `examples/` - Working code examples
- `generated_images/` - AI-generated product images (gitignored)

## Strategic Documents

- `TSHIRT_STRATEGIC_PLAN.md` - Full business strategy (trend research, pricing, marketing)
- `COTTAGE_CORE_GOTH_DESIGNS.md` - Design concepts and specifications
- `SHOPIFY_SETUP_README.md` - E-commerce setup guide

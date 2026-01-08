# The Office - AI Business Agent Suite

An AI-powered business management system featuring autonomous agents that handle different aspects of running a small business.

## Agent Suite

### CEO Agent
Final decision maker who aggregates inputs from all agents.
- **Metrics Focus:** Customer satisfaction, operational efficiency, financial performance
- **Responsibilities:** Strategic planning, financial oversight, revenue/cost analysis, final decision authority

### Chief Product Officer (CPO) Agent
Product and customer-focused leader.
- **Metrics Focus:** Product-market fit, customer retention, conversion rates
- **Responsibilities:** Customer research, product design, pricing, marketing campaigns, customer success, UI/UX optimization

### Chief Technology Officer (CTO) Agent
Infrastructure and operations leader.
- **Metrics Focus:** System reliability, operational efficiency, error rates
- **Responsibilities:** Agent development, skills library, automation, inter-agent communication, quality control, process optimization

## Architecture

The system uses a modular architecture where:
- Each agent operates independently with specific responsibilities
- Agents communicate through a shared messaging system
- Metrics are tracked and reported centrally
- The CEO agent makes final decisions based on inputs from all agents

## Getting Started

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd the-office

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### Run Demo

```bash
python main.py
```

### Quick Start Example

```python
from src.business import Business

# Initialize the business
business = Business()

# Record metrics
business.record_metrics({
    'customer': {'retention_rate': 0.85, 'churn_rate': 0.15},
    'financial': {'profit_margin': 0.30, 'revenue': 100000}
})

# Get CEO's business review
review = business.review_business()
print(review)

# Analyze customer feedback
feedback = [
    {"text": "Love the product!", "rating": "5"},
    {"text": "Checkout is confusing", "rating": "3"}
]
analysis = business.analyze_customer_feedback(feedback)
print(analysis)
```

## Documentation

- **[Architecture Guide](docs/ARCHITECTURE.md)** - System design, components, and data flow
- **[Usage Guide](docs/USAGE_GUIDE.md)** - Detailed usage instructions and examples

## Examples

The `examples/` directory contains complete working examples:

- `basic_usage.py` - Basic operations and metrics tracking
- `strategic_planning.py` - CEO strategic planning and decision making
- `product_development.py` - Feature development with CPO/CTO collaboration
- `operations_automation.py` - CTO automation and infrastructure design

Run any example:
```bash
python examples/basic_usage.py
```

## Features

- **Autonomous Agents**: CEO, CPO, and CTO agents with specialized capabilities
- **Inter-Agent Communication**: Message bus for seamless collaboration
- **Metrics Tracking**: Centralized tracking of customer, operational, and financial metrics
- **Strategic Decision Making**: Data-driven decisions based on business goals
- **AI-Powered Reasoning**: Each agent uses Claude to analyze and solve problems

## Use Cases

- Strategic planning and goal setting
- Customer feedback analysis
- Product feature design and development
- Pricing optimization
- Marketing campaign planning
- Process automation
- Technical feasibility assessment
- Performance optimization
- Error rate reduction

## Requirements

- Python 3.8+
- Anthropic API key
- Dependencies listed in requirements.txt

## License

MIT License

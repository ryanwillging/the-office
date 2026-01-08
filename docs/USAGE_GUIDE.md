# Usage Guide

## Quick Start

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

### Basic Usage

```python
from src.business import Business

# Initialize the business
business = Business()

# Record current metrics
business.record_metrics({
    'customer': {
        'retention_rate': 0.85,
        'churn_rate': 0.15,
        'conversion_rate': 0.14
    },
    'financial': {
        'profit_margin': 0.30,
        'revenue': 100000
    }
})

# Get business review from CEO
review = business.review_business()
print(review)
```

## Common Use Cases

### 1. Customer Feedback Analysis

```python
# Collect customer feedback
feedback = [
    {"text": "Love the product but checkout is confusing", "rating": "4"},
    {"text": "Great customer support!", "rating": "5"},
    {"text": "App is slow on mobile", "rating": "3"}
]

# CPO analyzes feedback
analysis = business.analyze_customer_feedback(feedback)
print(analysis)
```

**Output:** Analysis with themes, pain points, feature requests, and recommendations.

### 2. Feature Development

```python
# CPO designs a feature
feature = business.design_feature(
    feature="Dark mode with auto-switching",
    problem="Users report eye strain at night"
)

# This automatically:
# 1. CPO creates UX design
# 2. Sends to CTO for technical assessment
# 3. CTO responds with feasibility

# Process messages to get CTO's response
responses = business.process_all_messages()
print(responses['CTO'])
```

### 3. Strategic Planning

```python
# Set quarterly strategy
strategy = business.set_strategy(
    period="Q1 2026",
    focus_areas=[
        "Reduce churn to 15%",
        "Launch mobile app",
        "Improve conversion rate"
    ]
)
print(strategy)

# Make a strategic decision
decision = business.make_decision(
    topic="Invest in mobile app or improve web?",
    context={
        "mobile_traffic": 0.45,
        "available_budget": 50000
    }
)
print(decision['decision'])
```

### 4. Operational Automation

```python
# CTO designs automation
automation = business.create_automation(
    task="Daily metrics reporting",
    frequency="Daily at 9am",
    process="Manual: Login, export, calculate, email"
)
print(automation['automation'])
```

### 5. Creating New Agents

```python
# CTO designs a new agent
new_agent = business.cto.design_agent(
    goal="Prevent customer churn proactively",
    responsibilities=[
        "Monitor engagement metrics",
        "Identify at-risk customers",
        "Trigger retention campaigns"
    ]
)
print(new_agent['design'])
```

## Working with Individual Agents

### CEO Agent

```python
ceo = business.get_agent("CEO")

# Review metrics
review = ceo.review_metrics()

# Make a decision
decision = ceo.make_decision(
    "Should we expand to enterprise market?",
    context={"current_revenue": 100000, "enterprise_opportunity": 500000}
)

# Set strategy
strategy = ceo.set_strategy("2026", ["Growth", "Efficiency"])
```

### CPO Agent

```python
cpo = business.get_agent("CPO")

# Optimize pricing
pricing = cpo.optimize_pricing(
    current_pricing={"basic": 9.99, "pro": 29.99},
    market_data={"competitor_basic": 12.99}
)

# Create marketing campaign
campaign = cpo.create_marketing_campaign(
    goal="Increase signups by 20%",
    target_audience="Small businesses",
    budget=10000
)

# Improve retention
retention_plan = cpo.improve_retention(
    churn_data={"top_reason": "lack of features"}
)

# Review UX
ux_improvements = cpo.review_ux(
    user_journey="Homepage → Signup → Onboarding → Dashboard",
    pain_points=["Onboarding is too long", "Dashboard is cluttered"]
)
```

### CTO Agent

```python
cto = business.get_agent("CTO")

# Create a reusable skill
skill = cto.create_skill(
    skill_name="CustomerSegmentation",
    purpose="Segment customers by behavior and value",
    use_cases=["VIP treatment", "Retention campaigns"]
)

# Assess technical feasibility
assessment = cto.assess_technical_feasibility({
    "feature": "Real-time collaboration",
    "requirements": ["Low latency", "Multi-user"]
})

# Reduce error rate
error_plan = cto.reduce_error_rate({
    "current_rate": 0.03,
    "top_errors": ["API timeout", "Database deadlock"]
})

# Optimize performance
perf_plan = cto.optimize_performance({
    "avg_response_time": 250,
    "target": 100
})
```

## Inter-Agent Communication

Agents communicate through the message bus:

```python
# Send a message
cpo = business.get_agent("CPO")
cpo.send_message(
    to_agent="CTO",
    subject="Performance issue on mobile",
    content={"page": "checkout", "load_time": "5s"},
    message_type=MessageType.REQUEST,
    requires_response=True
)

# Process all messages
responses = business.process_all_messages()

# View conversation thread
# (Access message bus directly for advanced usage)
messages = business.message_bus.get_messages_for("CTO")
for msg in messages:
    print(f"From: {msg.from_agent}, Subject: {msg.subject}")
```

## Metrics Tracking

### Recording Metrics

```python
# Record customer metrics
business.record_metrics({
    'customer': {
        'retention_rate': 0.85,
        'churn_rate': 0.15,
        'conversion_rate': 0.14,
        'nps_score': 42
    }
})

# Record financial metrics
business.record_metrics({
    'financial': {
        'revenue': 100000,
        'costs': 70000,
        'profit_margin': 0.30
    }
})

# Record operational metrics
business.record_metrics({
    'operational': {
        'error_rate': 0.02,
        'uptime': 0.999,
        'support_ticket_volume': 45
    }
})
```

### Accessing Metrics

```python
# Get latest value for a metric
tracker = business.metrics_tracker
retention = tracker.get_latest('retention_rate')
print(f"Current retention: {retention.value}")

# Get all metrics by category
customer_metrics = tracker.get_by_category('customer')

# Get summary of all metrics
summary = tracker.get_summary()
print(summary)
# {
#   'customer': {'retention_rate': 0.85, ...},
#   'operational': {'error_rate': 0.02, ...},
#   'financial': {'profit_margin': 0.30, ...}
# }
```

## Business Status

```python
# Get overall business status
status = business.get_business_status()

print(f"Total messages: {status['total_messages']}")
print(f"Metrics recorded: {status['total_metrics_recorded']}")
print(f"Pending messages by agent: {status['pending_messages']}")
print(f"Current metrics: {status['metrics']}")
```

## Advanced Usage

### Custom Agent Prompts

Agents can be given specific prompts:

```python
ceo = business.get_agent("CEO")

# Ask CEO a specific question
response = ceo.think(
    "What are the top 3 priorities for the business right now?",
    context={"quarter": "Q1 2026", "runway_months": 18}
)
print(response)
```

### Broadcast Messages

```python
# CEO broadcasts to all agents
business.message_bus.broadcast(
    from_agent="CEO",
    subject="New company goal: 95% customer satisfaction",
    content={"target": 0.95, "deadline": "Q2 2026"},
    message_type=MessageType.NOTIFICATION
)
```

### Custom Metrics Categories

You can extend the system with custom categories:

```python
# Just specify the category when recording
business.metrics_tracker.record(
    name="team_satisfaction",
    value=4.5,
    category="hr",  # Custom category
    source_agent="CEO"
)
```

## Best Practices

1. **Record metrics regularly** - Helps agents make informed decisions
2. **Process messages periodically** - Call `process_all_messages()` after major operations
3. **Provide context** - Include relevant data when requesting decisions or analysis
4. **Review outputs** - Agent responses are LLM-generated; validate critical decisions
5. **Use appropriate agents** - Route tasks to the right agent (customer → CPO, tech → CTO)
6. **Monitor API usage** - Each `think()` call uses Claude API credits

## Error Handling

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Check for API key
if not os.getenv("ANTHROPIC_API_KEY"):
    raise ValueError("ANTHROPIC_API_KEY not found")

# Wrap agent calls in try/except
try:
    review = business.review_business()
except Exception as e:
    print(f"Error getting business review: {e}")
```

## Examples

See the `examples/` directory for complete working examples:

- `basic_usage.py` - Simple usage patterns
- `strategic_planning.py` - CEO strategic planning
- `product_development.py` - Feature development workflow
- `operations_automation.py` - CTO automation and infrastructure

Run examples:
```bash
python examples/basic_usage.py
python examples/strategic_planning.py
```

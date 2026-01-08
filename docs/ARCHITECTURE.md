# Architecture Documentation

## Overview

The Office is an AI-powered business management system featuring autonomous agents that collaborate to run a small business.

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Business Orchestrator                 │
│                     (src/business.py)                    │
└─────────────────────────────────────────────────────────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
      ┌────▼────┐     ┌────▼────┐     ┌───▼─────┐
      │   CEO   │     │   CPO   │     │   CTO   │
      │  Agent  │     │  Agent  │     │  Agent  │
      └────┬────┘     └────┬────┘     └───┬─────┘
           │               │               │
           └───────────────┼───────────────┘
                           │
           ┌───────────────┴───────────────┐
           │                               │
      ┌────▼────────┐              ┌───────▼────────┐
      │  Message    │              │    Metrics     │
      │     Bus     │              │    Tracker     │
      └─────────────┘              └────────────────┘
```

## Core Components

### 1. Message Bus (`src/core/messaging.py`)

The message bus enables inter-agent communication through a centralized messaging system.

**Features:**
- Typed messages (REQUEST, RESPONSE, NOTIFICATION, DECISION_NEEDED, DECISION_MADE)
- Priority levels (LOW, NORMAL, HIGH, URGENT)
- Conversation threading
- Broadcast capabilities

**Message Flow:**
1. Agent sends message via `message_bus.send()`
2. Message stored centrally
3. Target agent retrieves with `get_messages_for()`
4. Agent can respond, creating a conversation thread

### 2. Metrics Tracker (`src/core/metrics.py`)

Centralized system for tracking business metrics.

**Metric Categories:**
- **Customer:** Retention, churn, conversion, satisfaction
- **Operational:** Error rates, efficiency, costs
- **Financial:** Revenue, profit margin, cash flow

**Features:**
- Time-stamped metric recording
- Category-based organization
- Source agent tracking
- Summary generation by category

### 3. Base Agent (`src/agents/base_agent.py`)

Abstract base class that all agents inherit from.

**Key Methods:**
- `think(prompt, context)`: Uses Claude to reason through problems
- `process_messages()`: Handles incoming messages
- `send_message()`: Sends messages to other agents
- `record_metric()`: Records business metrics
- `get_system_prompt()`: Returns agent's role and responsibilities (abstract)

**Agent Lifecycle:**
1. Initialize with config, message bus, and metrics tracker
2. Receive prompts or messages
3. Think through problems using Claude API
4. Take actions (send messages, record metrics)
5. Store context for future reference

## Agent Specifications

### CEO Agent (`src/agents/ceo.py`)

**Role:** Final decision maker and strategic leader

**Responsibilities:**
- Strategic planning and business direction
- Financial oversight and budget planning
- Revenue and cost optimization
- Coordination between agents
- Final decision authority

**Key Methods:**
- `make_decision(topic, context)`: Makes strategic decisions
- `review_metrics()`: Analyzes business health
- `set_strategy(period, focus_areas)`: Sets strategic direction

**Decision Making Process:**
1. Requests input from CPO and CTO
2. Analyzes customer, operational, and financial impact
3. Makes data-driven decision
4. Broadcasts decision to all agents

### CPO Agent (`src/agents/cpo.py`)

**Role:** Product and customer leader

**Responsibilities:**
- Customer research and feedback analysis
- Product design and development
- Pricing strategy
- Marketing and customer acquisition
- Customer success and retention
- UI/UX optimization

**Key Methods:**
- `analyze_customer_feedback(feedback)`: Analyzes customer input
- `design_feature(feature, problem)`: Designs new features
- `optimize_pricing(current, market_data)`: Optimizes pricing
- `create_marketing_campaign(goal, audience, budget)`: Plans campaigns
- `improve_retention(churn_data)`: Develops retention strategies
- `review_ux(journey, pain_points)`: Improves user experience

**Focus:** Customer-obsessed, design-focused, data-driven

### CTO Agent (`src/agents/cto.py`)

**Role:** Infrastructure and operations leader

**Responsibilities:**
- Building AI-first infrastructure
- Creating agents and skills library
- Developing automations
- Inter-agent communication systems
- Operational efficiency
- Quality control and monitoring

**Key Methods:**
- `design_agent(goal, responsibilities)`: Designs new agents
- `create_skill(name, purpose, use_cases)`: Creates reusable skills
- `design_automation(task, frequency, process)`: Automates tasks
- `assess_technical_feasibility(request)`: Evaluates feasibility
- `reduce_error_rate(error_data)`: Improves reliability
- `optimize_performance(data)`: Enhances performance
- `improve_agent_communication()`: Upgrades messaging system
- `build_analytics(metrics, stakeholders)`: Creates analytics

**Focus:** Technical excellence, automation, quality, scalability

## Data Flow Examples

### Example 1: Feature Request Flow

```
1. CPO designs feature
   └─> CPO.design_feature("dark mode", "eye strain at night")

2. CPO sends message to CTO
   └─> Message(to="CTO", type=REQUEST, subject="Technical feasibility")

3. CTO receives and processes message
   └─> CTO.process_messages()
   └─> CTO.assess_technical_feasibility()

4. CTO responds with assessment
   └─> Message(to="CPO", type=RESPONSE, subject="Re: Technical feasibility")

5. If needed, escalate to CEO for decision
   └─> Message(to="CEO", type=DECISION_NEEDED)

6. CEO makes final decision
   └─> CEO.make_decision()
   └─> Broadcast(type=DECISION_MADE)
```

### Example 2: Metrics Review Flow

```
1. Record metrics
   └─> metrics_tracker.record("retention_rate", 0.85, "customer", "CPO")
   └─> metrics_tracker.record("error_rate", 0.02, "operational", "CTO")

2. CEO reviews business
   └─> CEO.review_metrics()
   └─> Gets metrics_summary from tracker
   └─> Analyzes using Claude

3. CEO provides insights
   └─> Broadcasts findings to all agents

4. Agents respond with action plans
   └─> CPO: retention improvement plan
   └─> CTO: error reduction strategy
```

## Extension Points

### Adding New Agents

1. Create new agent class inheriting from `BaseAgent`
2. Implement `get_system_prompt()` with role definition
3. Add agent-specific methods
4. Register in `Business` orchestrator
5. Update category mappings in `record_metrics()`

### Adding New Skills (CTO-managed)

1. Define skill specification using `CTO.create_skill()`
2. Implement skill as a module
3. Make available to relevant agents
4. Document in skills library

### Adding New Metrics

1. Choose category: customer, operational, or financial
2. Record via `metrics_tracker.record(name, value, category, agent)`
3. Access via `metrics_tracker.get_latest(name)` or `get_summary()`

## Best Practices

1. **Agents should communicate through the message bus** - Avoid direct method calls between agents
2. **Record metrics regularly** - This informs decision-making
3. **Use typed messages** - Helps with message routing and handling
4. **Provide context** - Include relevant data when requesting decisions
5. **Process messages periodically** - Call `process_all_messages()` regularly
6. **Review conversation threads** - Use `message_bus.get_conversation()` to understand decision history

## Performance Considerations

- **API Calls:** Each `think()` call makes a Claude API request
- **Message Volume:** Large message volumes may need pagination
- **Metric Storage:** In-memory storage; consider persistence for production
- **Context Management:** Agent context grows over time; may need truncation

## Security Considerations

- **API Key Management:** Store ANTHROPIC_API_KEY securely in .env
- **Message Validation:** Validate message content to prevent injection
- **Access Control:** Future: Add role-based access for agent actions
- **Data Privacy:** Customer data in metrics should be anonymized

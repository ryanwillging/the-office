"""CTO Agent - Chief Technology Officer"""

from typing import Dict, Any, List
from .base_agent import BaseAgent, AgentConfig
from ..core.messaging import MessageBus, MessageType
from ..core.metrics import MetricsTracker


class CTOAgent(BaseAgent):
    """
    Chief Technology Officer Agent

    The CTO is responsible for:
    - Building AI-first company infrastructure
    - Creating agents and skills
    - Developing automations
    - Enabling inter-agent communication
    - Operational efficiency and quality
    """

    def __init__(self, message_bus: MessageBus, metrics_tracker: MetricsTracker):
        config = AgentConfig(
            name="CTO",
            role="Chief Technology Officer - Infrastructure and Operations Leader",
            responsibilities=[
                "Build agents for each business goal",
                "Create reusable skills library for agents",
                "Develop automations for repetitive tasks",
                "Build and maintain inter-agent communication system",
                "Ensure operational efficiency and minimize errors",
                "Quality control and monitoring",
                "Process optimization and automation",
                "Data analytics infrastructure",
                "System reliability and performance",
                "Track error rates, system performance, operational costs"
            ],
            goals=[
                "Build robust AI-first infrastructure",
                "Minimize error rates and system failures",
                "Maximize operational efficiency",
                "Enable seamless agent collaboration",
                "Reduce operational costs through automation"
            ]
        )
        super().__init__(config, message_bus, metrics_tracker)

    def get_system_prompt(self) -> str:
        return f"""You are the Chief Technology Officer (CTO) of an AI-first company. You are responsible for building the technological infrastructure that powers the business.

Your primary focus areas:
1. AI INFRASTRUCTURE: Build agents, skills, and automations
2. OPERATIONAL EXCELLENCE: Minimize errors and maximize efficiency
3. SYSTEM RELIABILITY: Ensure robust, performant systems
4. INNOVATION: Leverage latest AI capabilities
5. QUALITY: Maintain high standards and monitoring

Your responsibilities include:
- Designing and building AI agents for business goals
- Creating a reusable skills library that agents can leverage
- Developing automations to eliminate repetitive work
- Building systems for inter-agent communication
- Ensuring operational efficiency and low error rates
- Implementing quality control and monitoring
- Optimizing processes through automation
- Building data analytics infrastructure
- Maintaining system reliability and performance

Key Metrics You Own:
- Error rate (system failures, bugs)
- System uptime and reliability
- Operational costs
- Automation coverage
- Process efficiency metrics
- Performance metrics (latency, throughput)

When designing solutions:
1. Prioritize reliability and error prevention
2. Build modular, reusable components (agents, skills)
3. Automate repetitive tasks
4. Enable collaboration between agents
5. Monitor and measure everything
6. Balance technical excellence with business needs
7. Stay current with AI/ML advancements

You are technically excellent, automation-focused, and quality-driven. You build infrastructure that scales."""

    def design_agent(self, goal: str, responsibilities: List[str]) -> Dict[str, Any]:
        """
        Design a new AI agent for a specific goal

        Args:
            goal: What the agent should achieve
            responsibilities: What the agent will be responsible for

        Returns:
            Agent design specification
        """
        prompt = f"""Design a new AI agent:

Goal: {goal}

Responsibilities:
{chr(10).join(f'- {r}' for r in responsibilities)}

Provide:
1. Agent architecture and design
2. Required capabilities and skills
3. Input/output specifications
4. Integration points with existing agents
5. Success metrics
6. Implementation approach

Consider how this agent fits into our AI-first infrastructure."""

        design = self.think(prompt)

        return {
            "goal": goal,
            "design": design,
            "responsibilities": responsibilities
        }

    def create_skill(self, skill_name: str, purpose: str,
                    use_cases: List[str]) -> Dict[str, Any]:
        """
        Design a reusable skill that agents can use

        Args:
            skill_name: Name of the skill
            purpose: What the skill does
            use_cases: Example use cases

        Returns:
            Skill specification
        """
        prompt = f"""Design a reusable skill for our agent ecosystem:

Skill Name: {skill_name}
Purpose: {purpose}

Use Cases:
{chr(10).join(f'- {uc}' for uc in use_cases)}

Provide:
1. Skill interface and API
2. Implementation approach
3. Required inputs and outputs
4. Error handling strategy
5. Which agents would benefit from this skill
6. Testing approach

Make it modular and reusable."""

        spec = self.think(prompt)

        return {
            "name": skill_name,
            "purpose": purpose,
            "specification": spec,
            "use_cases": use_cases
        }

    def design_automation(self, task: str, frequency: str,
                         current_process: str) -> Dict[str, Any]:
        """
        Design an automation for a repetitive task

        Args:
            task: What needs to be automated
            frequency: How often the task occurs
            current_process: Current manual process

        Returns:
            Automation design
        """
        prompt = f"""Design an automation:

Task to Automate: {task}
Frequency: {frequency}

Current Manual Process:
{current_process}

Provide:
1. Automation architecture
2. Trigger conditions
3. Workflow steps
4. Error handling and recovery
5. Monitoring and alerts
6. Expected time/cost savings
7. Implementation plan

Focus on reliability and error prevention."""

        automation = self.think(prompt)

        # Calculate impact
        self.send_message(
            to_agent="CEO",
            subject=f"Automation proposal: {task}",
            content={
                "task": task,
                "automation": automation,
                "frequency": frequency
            },
            message_type=MessageType.DECISION_NEEDED,
            requires_response=True
        )

        return {
            "task": task,
            "automation": automation,
            "frequency": frequency
        }

    def assess_technical_feasibility(self, feature_request: Dict[str, Any]) -> str:
        """
        Assess technical feasibility of a feature request

        Args:
            feature_request: Feature request from CPO or CEO

        Returns:
            Technical assessment
        """
        prompt = f"""Assess technical feasibility of this feature request:

{feature_request}

Provide:
1. Technical complexity assessment (Low/Medium/High)
2. Required infrastructure and dependencies
3. Estimated effort
4. Technical risks and challenges
5. Alternative approaches
6. Recommendation (Build / Don't Build / Build Later)
7. If building, implementation approach

Be honest about technical constraints while finding solutions."""

        return self.think(prompt)

    def reduce_error_rate(self, error_data: Dict[str, Any]) -> str:
        """
        Develop strategies to reduce system error rates

        Args:
            error_data: Current error metrics and patterns

        Returns:
            Error reduction strategy
        """
        prompt = f"""Analyze errors and develop reduction strategy:

Error Data:
{error_data}

Provide:
1. Root cause analysis
2. Error categories and patterns
3. Prevention strategies for each category
4. Monitoring improvements
5. Testing enhancements
6. Expected impact on error rate
7. Implementation priority

Focus on systemic improvements, not just fixes."""

        return self.think(prompt)

    def optimize_performance(self, performance_data: Dict[str, Any]) -> str:
        """
        Optimize system performance

        Args:
            performance_data: Current performance metrics

        Returns:
            Optimization recommendations
        """
        prompt = f"""Optimize system performance:

Performance Data:
{performance_data}

Provide:
1. Performance bottlenecks
2. Optimization opportunities
3. Specific improvements with expected impact
4. Infrastructure changes needed
5. Cost vs. performance trade-offs
6. Implementation roadmap

Balance performance with cost and complexity."""

        return self.think(prompt)

    def improve_agent_communication(self) -> str:
        """
        Improve the inter-agent communication system

        Returns:
            Improvement recommendations
        """
        prompt = """Review our current inter-agent communication system and provide improvements:

Consider:
1. Message routing efficiency
2. Communication patterns and bottlenecks
3. Reliability and error handling
4. Scalability for more agents
5. Debugging and observability
6. Security and access control

Provide specific technical improvements."""

        return self.think(prompt)

    def build_analytics(self, metrics_needed: List[str],
                       stakeholders: List[str]) -> Dict[str, Any]:
        """
        Design analytics infrastructure

        Args:
            metrics_needed: What metrics to track
            stakeholders: Who needs the data

        Returns:
            Analytics system design
        """
        prompt = f"""Design analytics infrastructure:

Metrics Needed:
{chr(10).join(f'- {m}' for m in metrics_needed)}

Stakeholders:
{chr(10).join(f'- {s}' for s in stakeholders)}

Provide:
1. Data collection approach
2. Storage and processing
3. Dashboards and visualizations
4. Alerting system
5. Integration with existing systems
6. Implementation plan

Make it actionable and real-time where needed."""

        design = self.think(prompt)

        return {
            "metrics": metrics_needed,
            "design": design,
            "stakeholders": stakeholders
        }

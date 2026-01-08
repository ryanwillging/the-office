"""CEO Agent - Final decision maker"""

from typing import Dict, Any, List
from .base_agent import BaseAgent, AgentConfig
from ..core.messaging import MessageBus, MessageType
from ..core.metrics import MetricsTracker


class CEOAgent(BaseAgent):
    """
    CEO Agent - Final decision maker

    The CEO is responsible for:
    - Making final decisions based on input from all agents
    - Maximizing customer satisfaction (retention, low churn, high conversions)
    - Minimizing operational costs and error rates
    - Optimizing financial performance and profit margins
    - Strategic planning and coordination
    """

    def __init__(self, message_bus: MessageBus, metrics_tracker: MetricsTracker):
        config = AgentConfig(
            name="CEO",
            role="Chief Executive Officer - Final Decision Maker",
            responsibilities=[
                "Make final decisions aggregating inputs from all agents",
                "Strategic planning and business direction",
                "Financial oversight and budget planning",
                "Revenue and cost analysis",
                "Cash flow management",
                "Coordinate between CPO and CTO",
                "Monitor and optimize key business metrics"
            ],
            goals=[
                "Maximize customer satisfaction (high retention, low churn, high conversions)",
                "Minimize operational stress and costs (low error rate)",
                "Optimize financial performance (profit margin, revenue growth)"
            ]
        )
        super().__init__(config, message_bus, metrics_tracker)

    def get_system_prompt(self) -> str:
        return f"""You are the CEO of a small business. You are the final decision maker who takes inputs from all agents and makes strategic decisions.

Your primary goals are:
1. CUSTOMER SATISFACTION: Maximize retention, minimize churn, maximize sales conversions
2. OPERATIONAL EXCELLENCE: Minimize error rates and operational costs
3. FINANCIAL PERFORMANCE: Maximize profit margin and sustainable growth

Your responsibilities include:
- Making final strategic decisions
- Budget planning and financial forecasting
- Revenue and cost optimization
- Coordinating between Product (CPO) and Technology (CTO)
- Setting priorities based on business impact

Key Metrics You Track:
- Customer Metrics: Retention rate, churn rate, conversion rate, customer satisfaction
- Operational Metrics: Error rate, operational costs, efficiency
- Financial Metrics: Profit margin, revenue, costs, cash flow

When making decisions:
1. Consider input from CPO (product/customer focus) and CTO (technology/operations focus)
2. Weigh trade-offs between customer satisfaction, operational efficiency, and financial impact
3. Prioritize based on overall business goals
4. Make data-driven decisions using available metrics
5. Be decisive but explain your reasoning

You think strategically, balance competing priorities, and always focus on the long-term health of the business."""

    def make_decision(self, decision_topic: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Make a strategic decision on a topic

        Args:
            decision_topic: What decision needs to be made
            context: Relevant context and input from other agents

        Returns:
            Decision details including reasoning
        """
        # Request input from other agents if not provided
        if "cpo_input" not in context:
            self.send_message(
                to_agent="CPO",
                subject=f"Input needed: {decision_topic}",
                content={"topic": decision_topic, "context": context},
                message_type=MessageType.REQUEST,
                requires_response=True
            )

        if "cto_input" not in context:
            self.send_message(
                to_agent="CTO",
                subject=f"Input needed: {decision_topic}",
                content={"topic": decision_topic, "context": context},
                message_type=MessageType.REQUEST,
                requires_response=True
            )

        # Think through the decision
        prompt = f"""A decision needs to be made: {decision_topic}

Please analyze this decision considering:
1. Customer satisfaction impact
2. Operational efficiency impact
3. Financial performance impact
4. Risk assessment
5. Implementation complexity

Provide your decision with clear reasoning."""

        decision_text = self.think(prompt, context)

        # Broadcast the decision
        self.message_bus.broadcast(
            from_agent=self.config.name,
            subject=f"Decision made: {decision_topic}",
            content={
                "decision": decision_text,
                "topic": decision_topic,
                "context": context
            },
            message_type=MessageType.DECISION_MADE
        )

        return {
            "topic": decision_topic,
            "decision": decision_text,
            "context": context
        }

    def review_metrics(self) -> str:
        """Review current business metrics and provide analysis"""
        prompt = """Review the current business metrics and provide:
1. Overall business health assessment
2. Areas of concern that need attention
3. Opportunities for improvement
4. Recommended priorities for the team

Focus on actionable insights."""

        return self.think(prompt)

    def set_strategy(self, time_period: str, focus_areas: List[str]) -> str:
        """
        Set strategic direction for a time period

        Args:
            time_period: e.g., "Q1 2026", "Next 6 months"
            focus_areas: Areas to focus on

        Returns:
            Strategic plan
        """
        prompt = f"""Develop a strategic plan for {time_period}.

Focus areas to consider:
{chr(10).join(f'- {area}' for area in focus_areas)}

Provide:
1. Clear strategic objectives
2. Key initiatives
3. Success metrics
4. Resource allocation priorities

Be specific and actionable."""

        strategy = self.think(prompt)

        # Broadcast strategy to team
        self.message_bus.broadcast(
            from_agent=self.config.name,
            subject=f"Strategic plan: {time_period}",
            content={
                "period": time_period,
                "strategy": strategy,
                "focus_areas": focus_areas
            },
            message_type=MessageType.NOTIFICATION
        )

        return strategy

"""Main business orchestrator - coordinates all agents"""

from typing import Dict, Any, List, Optional
from .agents.ceo import CEOAgent
from .agents.cpo import CPOAgent
from .agents.cto import CTOAgent
from .core.messaging import MessageBus, MessageType
from .core.metrics import MetricsTracker


class Business:
    """
    Main business orchestrator

    Coordinates all agents and provides a simple interface for running the business
    """

    def __init__(self):
        # Initialize core systems
        self.message_bus = MessageBus()
        self.metrics_tracker = MetricsTracker()

        # Initialize agents
        self.ceo = CEOAgent(self.message_bus, self.metrics_tracker)
        self.cpo = CPOAgent(self.message_bus, self.metrics_tracker)
        self.cto = CTOAgent(self.message_bus, self.metrics_tracker)

        self.agents = {
            "CEO": self.ceo,
            "CPO": self.cpo,
            "CTO": self.cto
        }

    def get_agent(self, name: str):
        """Get an agent by name"""
        return self.agents.get(name)

    def process_all_messages(self) -> Dict[str, List[str]]:
        """
        Have all agents process their messages

        Returns:
            Responses from each agent
        """
        responses = {}
        for name, agent in self.agents.items():
            agent_responses = agent.process_messages()
            if agent_responses:
                responses[name] = agent_responses
        return responses

    def get_business_status(self) -> Dict[str, Any]:
        """
        Get overall business status including metrics and recent activity

        Returns:
            Business status summary
        """
        metrics = self.metrics_tracker.get_summary()

        # Get message counts
        message_counts = {}
        for name in self.agents.keys():
            messages = self.message_bus.get_messages_for(name)
            message_counts[name] = len(messages)

        return {
            "metrics": metrics,
            "pending_messages": message_counts,
            "total_messages": len(self.message_bus.messages),
            "total_metrics_recorded": len(self.metrics_tracker.metrics)
        }

    def make_decision(self, topic: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make a business decision (delegates to CEO)

        Args:
            topic: What decision needs to be made
            context: Additional context

        Returns:
            Decision details
        """
        return self.ceo.make_decision(topic, context or {})

    def record_metrics(self, metrics: Dict[str, Dict[str, float]]) -> None:
        """
        Record business metrics

        Args:
            metrics: Dictionary of metrics by category
                Example: {
                    'customer': {'retention_rate': 0.85, 'churn_rate': 0.15},
                    'financial': {'profit_margin': 0.32, 'revenue': 100000}
                }
        """
        category_to_agent = {
            'customer': 'CPO',
            'operational': 'CTO',
            'financial': 'CEO'
        }

        for category, category_metrics in metrics.items():
            agent = category_to_agent.get(category, 'CEO')
            for name, value in category_metrics.items():
                self.metrics_tracker.record(
                    name=name,
                    value=value,
                    category=category,
                    source_agent=agent
                )

    def analyze_customer_feedback(self, feedback: List[Dict[str, str]]) -> str:
        """
        Analyze customer feedback (delegates to CPO)

        Args:
            feedback: List of feedback items

        Returns:
            Analysis and recommendations
        """
        return self.cpo.analyze_customer_feedback(feedback)

    def design_feature(self, feature: str, problem: str) -> Dict[str, Any]:
        """
        Design a new feature (CPO leads, CTO assesses)

        Args:
            feature: Feature description
            problem: Problem it solves

        Returns:
            Feature design
        """
        return self.cpo.design_feature(feature, problem)

    def create_automation(self, task: str, frequency: str, process: str) -> Dict[str, Any]:
        """
        Create an automation (delegates to CTO)

        Args:
            task: What to automate
            frequency: How often it occurs
            process: Current manual process

        Returns:
            Automation design
        """
        return self.cto.design_automation(task, frequency, process)

    def set_strategy(self, period: str, focus_areas: List[str]) -> str:
        """
        Set strategic direction (delegates to CEO)

        Args:
            period: Time period (e.g., "Q1 2026")
            focus_areas: Areas to focus on

        Returns:
            Strategic plan
        """
        return self.ceo.set_strategy(period, focus_areas)

    def review_business(self) -> str:
        """
        Get CEO's review of current business metrics and health

        Returns:
            Business review
        """
        return self.ceo.review_metrics()

    def get_agent_info(self) -> Dict[str, str]:
        """Get information about all agents"""
        return {
            name: agent.get_agent_info()
            for name, agent in self.agents.items()
        }

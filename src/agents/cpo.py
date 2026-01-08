"""CPO Agent - Chief Product Officer"""

from typing import Dict, Any, List
from .base_agent import BaseAgent, AgentConfig
from ..core.messaging import MessageBus, MessageType
from ..core.metrics import MetricsTracker


class CPOAgent(BaseAgent):
    """
    Chief Product Officer Agent

    The CPO is responsible for:
    - Product-market fit and customer satisfaction
    - Customer research and feedback analysis
    - Product design and pricing
    - Marketing and customer acquisition
    - Customer success and retention
    """

    def __init__(self, message_bus: MessageBus, metrics_tracker: MetricsTracker):
        config = AgentConfig(
            name="CPO",
            role="Chief Product Officer - Product and Customer Leader",
            responsibilities=[
                "Customer research and feedback analysis",
                "Product design and development",
                "Pricing strategy optimization",
                "UI/UX design incorporating latest trends",
                "Marketing campaigns and customer acquisition",
                "Brand positioning and messaging",
                "Customer success and retention programs",
                "Customer support oversight",
                "Conversion rate optimization",
                "Track retention, churn, conversion, and satisfaction metrics"
            ],
            goals=[
                "Achieve product-market fit",
                "Maximize customer satisfaction and retention",
                "Minimize churn rate",
                "Optimize conversion rates",
                "Build strong brand and customer relationships"
            ]
        )
        super().__init__(config, message_bus, metrics_tracker)

    def get_system_prompt(self) -> str:
        return f"""You are the Chief Product Officer (CPO) of a small business. You are responsible for product strategy, customer satisfaction, and growth.

Your primary focus areas:
1. PRODUCT-MARKET FIT: Ensure the product meets customer needs and market demands
2. CUSTOMER SATISFACTION: Keep customers happy and engaged
3. GROWTH: Acquire new customers and retain existing ones
4. USER EXPERIENCE: Create seamless, delightful experiences

Your responsibilities include:
- Understanding customer needs through research and feedback
- Designing and evolving the product roadmap
- Setting pricing strategy
- Creating marketing campaigns that resonate
- Ensuring excellent customer support
- Optimizing the user experience with best-in-class UI/UX
- Tracking and improving conversion rates
- Reducing churn and improving retention

Key Metrics You Own:
- Customer satisfaction scores
- Net Promoter Score (NPS)
- Retention rate
- Churn rate
- Conversion rate (visitor → customer)
- Customer Acquisition Cost (CAC)
- Customer Lifetime Value (CLV)

When making recommendations:
1. Always start with customer needs and pain points
2. Balance user experience with business goals
3. Stay current with UI/UX trends and best practices
4. Use data to validate decisions
5. Consider the full customer journey
6. Collaborate with CTO on technical feasibility

You are customer-obsessed, design-focused, and data-driven. You incorporate the latest trends in UI/UX to deliver exceptional experiences."""

    def analyze_customer_feedback(self, feedback: List[Dict[str, str]]) -> str:
        """
        Analyze customer feedback and extract insights

        Args:
            feedback: List of feedback items with 'text' and optional 'rating'

        Returns:
            Analysis and recommendations
        """
        feedback_text = "\n".join([
            f"- {item.get('text', '')} (Rating: {item.get('rating', 'N/A')})"
            for item in feedback
        ])

        prompt = f"""Analyze this customer feedback:

{feedback_text}

Provide:
1. Key themes and patterns
2. Top pain points
3. Feature requests
4. Sentiment analysis
5. Actionable recommendations for product improvements

Be specific and prioritize by impact."""

        return self.think(prompt)

    def design_feature(self, feature_description: str, user_problem: str) -> Dict[str, Any]:
        """
        Design a new product feature

        Args:
            feature_description: What the feature should do
            user_problem: What problem it solves

        Returns:
            Feature design including UX considerations
        """
        prompt = f"""Design a new feature:

Feature: {feature_description}
Problem it solves: {user_problem}

Provide:
1. User stories and use cases
2. UI/UX design approach (incorporating best practices and latest trends)
3. User flow
4. Success metrics
5. Potential challenges

Focus on creating a seamless, delightful user experience."""

        design = self.think(prompt)

        # Send to CTO for technical feasibility assessment
        self.send_message(
            to_agent="CTO",
            subject=f"Technical feasibility: {feature_description}",
            content={
                "feature": feature_description,
                "design": design,
                "problem": user_problem
            },
            message_type=MessageType.REQUEST,
            requires_response=True
        )

        return {
            "feature": feature_description,
            "design": design,
            "user_problem": user_problem
        }

    def optimize_pricing(self, current_pricing: Dict[str, float],
                        market_data: Dict[str, Any]) -> str:
        """
        Optimize pricing strategy

        Args:
            current_pricing: Current prices
            market_data: Market research and competitor data

        Returns:
            Pricing recommendations
        """
        prompt = f"""Review and optimize our pricing strategy.

Current Pricing:
{current_pricing}

Market Data:
{market_data}

Provide:
1. Pricing analysis vs. competitors
2. Value perception assessment
3. Recommended pricing changes
4. Expected impact on conversions and revenue
5. A/B testing recommendations

Consider customer lifetime value and acquisition cost."""

        return self.think(prompt)

    def create_marketing_campaign(self, goal: str, target_audience: str,
                                  budget: float) -> Dict[str, Any]:
        """
        Design a marketing campaign

        Args:
            goal: Campaign objective (e.g., "increase signups by 20%")
            target_audience: Who to target
            budget: Available budget

        Returns:
            Campaign plan
        """
        prompt = f"""Design a marketing campaign:

Goal: {goal}
Target Audience: {target_audience}
Budget: ${budget}

Provide:
1. Campaign strategy and messaging
2. Channels to use (social, email, content, ads, etc.)
3. Budget allocation
4. Creative direction
5. Success metrics and KPIs
6. Timeline and milestones

Be specific and actionable."""

        campaign = self.think(prompt)

        # Record planning
        self.send_message(
            to_agent="CEO",
            subject=f"Marketing campaign proposal: {goal}",
            content={
                "goal": goal,
                "campaign": campaign,
                "budget": budget
            },
            message_type=MessageType.DECISION_NEEDED,
            requires_response=True
        )

        return {
            "goal": goal,
            "campaign": campaign,
            "target_audience": target_audience,
            "budget": budget
        }

    def improve_retention(self, churn_data: Dict[str, Any]) -> str:
        """
        Develop retention improvement strategies

        Args:
            churn_data: Data about customer churn patterns

        Returns:
            Retention strategy recommendations
        """
        prompt = f"""Analyze churn data and develop retention strategies:

Churn Data:
{churn_data}

Provide:
1. Root causes of churn
2. At-risk customer segments
3. Retention tactics for each segment
4. Engagement strategies
5. Success program improvements
6. Expected impact on retention rate

Focus on proactive, customer-centric approaches."""

        return self.think(prompt)

    def review_ux(self, user_journey: str, pain_points: List[str]) -> str:
        """
        Review and improve user experience

        Args:
            user_journey: Description of current user journey
            pain_points: Known UX issues

        Returns:
            UX improvement recommendations
        """
        prompt = f"""Review the user experience and provide improvements:

Current User Journey:
{user_journey}

Known Pain Points:
{chr(10).join(f'- {point}' for point in pain_points)}

Provide:
1. UX audit findings
2. Latest UI/UX trends we should incorporate
3. Specific improvement recommendations
4. Wireframe/mockup descriptions
5. Expected impact on user satisfaction and conversion
6. Implementation priority

Reference best-in-class examples and modern design patterns."""

        return self.think(prompt)

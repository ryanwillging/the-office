"""Base agent class for all business agents"""

from typing import Dict, List, Optional, Any
from abc import ABC, abstractmethod
import anthropic
import os
from pydantic import BaseModel

from ..core.messaging import MessageBus, Message, MessageType, MessagePriority
from ..core.metrics import MetricsTracker


class AgentConfig(BaseModel):
    """Configuration for an agent"""
    name: str
    role: str
    responsibilities: List[str]
    goals: List[str]
    model: str = "claude-sonnet-4-5-20250929"


class BaseAgent(ABC):
    """Base class for all business agents"""

    def __init__(self, config: AgentConfig, message_bus: MessageBus,
                 metrics_tracker: MetricsTracker):
        self.config = config
        self.message_bus = message_bus
        self.metrics_tracker = metrics_tracker
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.context: List[Dict[str, str]] = []

    @abstractmethod
    def get_system_prompt(self) -> str:
        """Get the system prompt for this agent"""
        pass

    def think(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Have the agent think through a problem using Claude

        Args:
            prompt: The question or task for the agent
            context: Additional context to include

        Returns:
            The agent's response
        """
        # Build context message
        context_str = ""
        if context:
            context_str = "\n\nContext:\n"
            for key, value in context.items():
                context_str += f"- {key}: {value}\n"

        # Add current metrics to context
        metrics_summary = self.metrics_tracker.get_summary()
        metrics_str = "\n\nCurrent Metrics:\n"
        for category, metrics in metrics_summary.items():
            metrics_str += f"\n{category.upper()}:\n"
            for name, value in metrics.items():
                metrics_str += f"  - {name}: {value}\n"

        full_prompt = f"{prompt}{context_str}{metrics_str}"

        # Call Claude
        message = self.client.messages.create(
            model=self.config.model,
            max_tokens=4000,
            system=self.get_system_prompt(),
            messages=[
                {"role": "user", "content": full_prompt}
            ]
        )

        response = message.content[0].text

        # Store in context
        self.context.append({
            "prompt": full_prompt,
            "response": response
        })

        return response

    def process_messages(self) -> List[str]:
        """
        Process incoming messages and generate responses

        Returns:
            List of response texts
        """
        messages = self.message_bus.get_messages_for(self.config.name)
        responses = []

        for msg in messages:
            if msg.requires_response:
                response_text = self.think(
                    f"You received a message from {msg.from_agent}:\n\n"
                    f"Subject: {msg.subject}\n\n"
                    f"Content: {msg.content}\n\n"
                    f"Please provide your response.",
                    context=msg.content
                )

                # Send response
                response_msg = Message(
                    from_agent=self.config.name,
                    to_agent=msg.from_agent,
                    message_type=MessageType.RESPONSE,
                    subject=f"Re: {msg.subject}",
                    content={"response": response_text},
                    in_response_to=msg.id
                )
                self.message_bus.send(response_msg)
                responses.append(response_text)

        return responses

    def send_message(self, to_agent: str, subject: str, content: Dict[str, Any],
                     message_type: MessageType = MessageType.NOTIFICATION,
                     requires_response: bool = False) -> None:
        """Send a message to another agent"""
        message = Message(
            from_agent=self.config.name,
            to_agent=to_agent,
            message_type=message_type,
            subject=subject,
            content=content,
            requires_response=requires_response
        )
        self.message_bus.send(message)

    def record_metric(self, name: str, value: float, category: str) -> None:
        """Record a metric"""
        self.metrics_tracker.record(
            name=name,
            value=value,
            category=category,
            source_agent=self.config.name
        )

    def get_agent_info(self) -> str:
        """Get formatted information about this agent"""
        info = f"Agent: {self.config.name}\n"
        info += f"Role: {self.config.role}\n\n"
        info += "Responsibilities:\n"
        for resp in self.config.responsibilities:
            info += f"  - {resp}\n"
        info += "\nGoals:\n"
        for goal in self.config.goals:
            info += f"  - {goal}\n"
        return info

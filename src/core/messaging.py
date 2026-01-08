"""Inter-agent communication system"""

from typing import Dict, List, Optional, Any
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum


class MessagePriority(str, Enum):
    """Message priority levels"""
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"


class MessageType(str, Enum):
    """Types of messages between agents"""
    REQUEST = "request"
    RESPONSE = "response"
    NOTIFICATION = "notification"
    DECISION_NEEDED = "decision_needed"
    DECISION_MADE = "decision_made"


class Message(BaseModel):
    """Message between agents"""
    id: str = Field(default_factory=lambda: f"msg_{datetime.now().timestamp()}")
    from_agent: str
    to_agent: str
    message_type: MessageType
    priority: MessagePriority = MessagePriority.NORMAL
    subject: str
    content: Dict[str, Any]
    timestamp: datetime = Field(default_factory=datetime.now)
    requires_response: bool = False
    in_response_to: Optional[str] = None


class MessageBus:
    """Central message bus for agent communication"""

    def __init__(self):
        self.messages: List[Message] = []
        self.subscribers: Dict[str, List[str]] = {}  # agent -> list of topics

    def send(self, message: Message) -> None:
        """Send a message to an agent"""
        self.messages.append(message)

    def get_messages_for(self, agent: str, unread_only: bool = True) -> List[Message]:
        """Get all messages for a specific agent"""
        messages = [m for m in self.messages if m.to_agent == agent]
        return messages

    def broadcast(self, from_agent: str, subject: str, content: Dict[str, Any],
                  message_type: MessageType = MessageType.NOTIFICATION) -> None:
        """Broadcast a message to all agents"""
        agents = ["CEO", "CPO", "CTO"]
        for agent in agents:
            if agent != from_agent:
                message = Message(
                    from_agent=from_agent,
                    to_agent=agent,
                    message_type=message_type,
                    subject=subject,
                    content=content
                )
                self.send(message)

    def get_conversation(self, message_id: str) -> List[Message]:
        """Get all messages in a conversation thread"""
        thread = []

        # Find the original message
        original = next((m for m in self.messages if m.id == message_id), None)
        if not original:
            return thread

        thread.append(original)

        # Find all responses
        def find_responses(msg_id: str):
            responses = [m for m in self.messages if m.in_response_to == msg_id]
            for resp in responses:
                thread.append(resp)
                find_responses(resp.id)

        find_responses(message_id)
        return thread

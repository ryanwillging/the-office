"""Metrics tracking and reporting system"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MetricData(BaseModel):
    """Individual metric data point"""
    name: str
    value: float
    timestamp: datetime = Field(default_factory=datetime.now)
    category: str  # 'customer', 'operational', 'financial'
    source_agent: str


class MetricsTracker:
    """Centralized metrics tracking system"""

    def __init__(self):
        self.metrics: List[MetricData] = []

    def record(self, name: str, value: float, category: str, source_agent: str) -> None:
        """Record a new metric"""
        metric = MetricData(
            name=name,
            value=value,
            category=category,
            source_agent=source_agent
        )
        self.metrics.append(metric)

    def get_latest(self, name: str) -> Optional[MetricData]:
        """Get the most recent value for a metric"""
        matching = [m for m in self.metrics if m.name == name]
        return matching[-1] if matching else None

    def get_by_category(self, category: str) -> List[MetricData]:
        """Get all metrics in a category"""
        return [m for m in self.metrics if m.category == category]

    def get_by_agent(self, agent: str) -> List[MetricData]:
        """Get all metrics from a specific agent"""
        return [m for m in self.metrics if m.source_agent == agent]

    def get_summary(self) -> Dict[str, Dict[str, float]]:
        """Get a summary of all latest metrics by category"""
        summary = {
            'customer': {},
            'operational': {},
            'financial': {}
        }

        # Get unique metric names
        metric_names = set(m.name for m in self.metrics)

        for name in metric_names:
            latest = self.get_latest(name)
            if latest:
                summary[latest.category][name] = latest.value

        return summary

#!/usr/bin/env python3
"""
Autonomous Build-Measure-Learn Loop
Runs The Office agents through continuous business iteration without human intervention.

Usage:
    python autonomous_loop.py --mode continuous
    python autonomous_loop.py --mode single-cycle
    python autonomous_loop.py --mode demo

Configuration:
    Set autonomy boundaries in .env:
    - AUTONOMOUS_BUDGET_LIMIT
    - LOOP_CADENCE (hourly, daily, weekly)
    - REQUIRE_HUMAN_APPROVAL (strategy, pricing, legal)
"""

import os
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

from src.business import Business
from src.core.messaging import MessageType, MessagePriority


class LoopPhase(Enum):
    """Phases of the Build-Measure-Learn loop"""
    MEASURE = "measure"
    LEARN = "learn"
    IDEAS = "ideas"
    BUILD = "build"


class LoopCadence(Enum):
    """How frequently the loop runs"""
    HOURLY = 3600  # Technical optimization loop
    DAILY = 86400  # Operational loop
    WEEKLY = 604800  # Product development loop
    QUARTERLY = 7776000  # Strategic planning loop


@dataclass
class LoopMetrics:
    """Metrics about the loop itself"""
    iteration_count: int = 0
    successful_iterations: int = 0
    failed_iterations: int = 0
    avg_cycle_time: float = 0.0
    decisions_made: int = 0
    autonomous_decisions: int = 0
    human_approvals_needed: int = 0
    business_improvement: float = 0.0


class AutonomousLoop:
    """
    Manages the autonomous Build-Measure-Learn loop for The Office.
    Orchestrates agents through continuous business iteration.
    """

    def __init__(
        self,
        business: Business,
        cadence: LoopCadence = LoopCadence.DAILY,
        autonomous_budget_limit: int = 500,
        require_approval_for: Optional[List[str]] = None,
    ):
        self.business = business
        self.cadence = cadence
        self.autonomous_budget_limit = autonomous_budget_limit
        self.require_approval_for = require_approval_for or [
            "strategy", "pricing", "legal", "budget_over_limit"
        ]

        self.loop_metrics = LoopMetrics()
        self.current_phase = LoopPhase.MEASURE
        self.iteration_start_time = None

        # Learning history
        self.learnings = []
        self.hypotheses = []
        self.validated_hypotheses = []
        self.invalidated_hypotheses = []

    def run_continuous(self):
        """Run the loop continuously at the configured cadence"""
        print(f"🔄 Starting continuous loop (cadence: {self.cadence.name})")
        print(f"💰 Autonomous budget limit: ${self.autonomous_budget_limit}")
        print(f"⚠️  Human approval required for: {', '.join(self.require_approval_for)}\n")

        while True:
            try:
                self.run_single_cycle()

                # Wait for next cycle
                wait_time = self.cadence.value
                next_run = datetime.now() + timedelta(seconds=wait_time)
                print(f"\n⏰ Next cycle at {next_run.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"💤 Sleeping for {wait_time}s...\n")
                time.sleep(wait_time)

            except KeyboardInterrupt:
                print("\n\n🛑 Loop stopped by user")
                self.print_summary()
                break
            except Exception as e:
                print(f"❌ Error in loop: {e}")
                self.loop_metrics.failed_iterations += 1
                time.sleep(60)  # Wait a minute before retrying

    def run_single_cycle(self) -> Dict:
        """Run one complete Build-Measure-Learn cycle"""
        self.iteration_start_time = datetime.now()
        self.loop_metrics.iteration_count += 1

        print("=" * 80)
        print(f"🔄 ITERATION #{self.loop_metrics.iteration_count}")
        print(f"⏰ Started at: {self.iteration_start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)

        try:
            # Phase 1: MEASURE
            measurement_data = self.measure_phase()

            # Phase 2: LEARN
            insights = self.learn_phase(measurement_data)

            # Phase 3: IDEAS
            decisions = self.ideas_phase(insights)

            # Phase 4: BUILD
            outputs = self.build_phase(decisions)

            # Complete iteration
            cycle_time = (datetime.now() - self.iteration_start_time).total_seconds()
            self.loop_metrics.successful_iterations += 1
            self.loop_metrics.avg_cycle_time = (
                (self.loop_metrics.avg_cycle_time * (self.loop_metrics.iteration_count - 1)
                 + cycle_time) / self.loop_metrics.iteration_count
            )

            print(f"\n✅ Cycle complete in {cycle_time:.1f}s")

            return {
                'success': True,
                'measurements': measurement_data,
                'insights': insights,
                'decisions': decisions,
                'outputs': outputs,
                'cycle_time': cycle_time,
            }

        except Exception as e:
            print(f"\n❌ Cycle failed: {e}")
            self.loop_metrics.failed_iterations += 1
            return {'success': False, 'error': str(e)}

    def measure_phase(self) -> Dict:
        """
        MEASURE Phase: Collect business metrics automatically
        Returns: Dictionary of collected metrics
        """
        self.current_phase = LoopPhase.MEASURE
        print("\n📏 MEASURE PHASE")
        print("-" * 80)

        measurements = {
            'customer': {},
            'operational': {},
            'financial': {},
            'timestamp': datetime.now().isoformat(),
        }

        # CTO: Collect technical/operational metrics
        print("⚙️  CTO: Collecting operational metrics...")
        try:
            # Simulate Shopify API call
            operational_metrics = self._collect_operational_metrics()
            measurements['operational'] = operational_metrics
            print(f"   ✓ Error rate: {operational_metrics.get('error_rate', 0):.2%}")
            print(f"   ✓ Response time: {operational_metrics.get('avg_response_time', 0)}ms")
        except Exception as e:
            print(f"   ✗ Failed to collect operational metrics: {e}")

        # CPO: Collect customer metrics
        print("👥 CPO: Collecting customer metrics...")
        try:
            customer_metrics = self._collect_customer_metrics()
            measurements['customer'] = customer_metrics
            print(f"   ✓ Conversion rate: {customer_metrics.get('conversion_rate', 0):.2%}")
            print(f"   ✓ Satisfaction: {customer_metrics.get('satisfaction', 0):.1f}/5")
        except Exception as e:
            print(f"   ✗ Failed to collect customer metrics: {e}")

        # CEO: Collect financial metrics
        print("📊 CEO: Collecting financial metrics...")
        try:
            financial_metrics = self._collect_financial_metrics()
            measurements['financial'] = financial_metrics
            print(f"   ✓ Revenue (period): ${financial_metrics.get('revenue', 0):,.2f}")
            print(f"   ✓ Profit margin: {financial_metrics.get('profit_margin', 0):.2%}")
        except Exception as e:
            print(f"   ✗ Failed to collect financial metrics: {e}")

        # Record measurements
        for category, metrics in measurements.items():
            if category != 'timestamp':
                for metric_name, value in metrics.items():
                    self.business.record_metric(metric_name, value, category)

        return measurements

    def learn_phase(self, measurement_data: Dict) -> Dict:
        """
        LEARN Phase: Analyze data and extract insights
        Returns: Dictionary of insights and patterns
        """
        self.current_phase = LoopPhase.LEARN
        print("\n🧠 LEARN PHASE")
        print("-" * 80)

        insights = {
            'ceo': {},
            'cpo': {},
            'cto': {},
            'patterns': [],
            'opportunities': [],
            'concerns': [],
        }

        # CEO: Business health review
        print("📊 CEO: Analyzing business health...")
        ceo_review = self.business.ceo.review_metrics()
        insights['ceo'] = {
            'summary': ceo_review,
            'health_score': self._calculate_health_score(measurement_data),
        }
        print(f"   Health score: {insights['ceo']['health_score']}/100")

        # CPO: Customer behavior analysis
        print("👥 CPO: Analyzing customer patterns...")
        customer_data = measurement_data.get('customer', {})
        cpo_insights = self._analyze_customer_patterns(customer_data)
        insights['cpo'] = cpo_insights

        if cpo_insights.get('patterns'):
            for pattern in cpo_insights['patterns']:
                print(f"   📊 Pattern: {pattern}")
                insights['patterns'].append(pattern)

        # CTO: Technical performance analysis
        print("⚙️  CTO: Analyzing technical performance...")
        operational_data = measurement_data.get('operational', {})
        cto_insights = self._analyze_technical_performance(operational_data)
        insights['cto'] = cto_insights

        # Identify opportunities and concerns
        insights['opportunities'] = self._identify_opportunities(measurement_data)
        insights['concerns'] = self._identify_concerns(measurement_data)

        if insights['opportunities']:
            print(f"\n💡 {len(insights['opportunities'])} opportunities identified")
            for opp in insights['opportunities']:
                print(f"   • {opp}")

        if insights['concerns']:
            print(f"\n⚠️  {len(insights['concerns'])} concerns detected")
            for concern in insights['concerns']:
                print(f"   • {concern}")

        # Store learnings
        self.learnings.append({
            'timestamp': datetime.now().isoformat(),
            'insights': insights,
            'metrics': measurement_data,
        })

        return insights

    def ideas_phase(self, insights: Dict) -> List[Dict]:
        """
        IDEAS Phase: Make decisions based on learnings
        Returns: List of decisions to execute
        """
        self.current_phase = LoopPhase.IDEAS
        print("\n💡 IDEAS PHASE")
        print("-" * 80)

        decisions = []

        # CEO: Strategic decisions based on opportunities and concerns
        print("📊 CEO: Making strategic decisions...")

        # Process opportunities
        for opportunity in insights.get('opportunities', []):
            decision = self._ceo_decide_on_opportunity(opportunity, insights)
            if decision:
                decisions.append(decision)
                print(f"   ✓ Decision: {decision['action']}")

                # Check if human approval needed
                if self._requires_human_approval(decision):
                    decision['status'] = 'pending_approval'
                    decision['autonomous'] = False
                    self.loop_metrics.human_approvals_needed += 1
                    print(f"   ⚠️  Requires human approval: {decision['reason']}")
                else:
                    decision['status'] = 'approved'
                    decision['autonomous'] = True
                    self.loop_metrics.autonomous_decisions += 1

        # Process concerns
        for concern in insights.get('concerns', []):
            decision = self._ceo_decide_on_concern(concern, insights)
            if decision:
                decisions.append(decision)
                print(f"   ⚠️  Addressing concern: {decision['action']}")

        self.loop_metrics.decisions_made += len(decisions)

        # Broadcast decisions via message bus
        for decision in decisions:
            if decision['status'] == 'approved':
                self.business.ceo.send_message(
                    to="ALL",
                    msg_type=MessageType.DECISION_MADE,
                    subject=decision['action'],
                    content=decision,
                    priority=MessagePriority.HIGH,
                )

        print(f"\n📊 {len(decisions)} decisions made")
        print(f"   Autonomous: {sum(1 for d in decisions if d.get('autonomous', False))}")
        print(f"   Requiring approval: {sum(1 for d in decisions if not d.get('autonomous', False))}")

        return decisions

    def build_phase(self, decisions: List[Dict]) -> List[Dict]:
        """
        BUILD Phase: Execute approved decisions
        Returns: List of outputs/products created
        """
        self.current_phase = LoopPhase.BUILD
        print("\n🔨 BUILD PHASE")
        print("-" * 80)

        outputs = []

        for decision in decisions:
            if decision['status'] != 'approved':
                print(f"⏭️  Skipping (not approved): {decision['action']}")
                continue

            print(f"\n🔨 Executing: {decision['action']}")

            try:
                output = self._execute_decision(decision)
                outputs.append(output)
                print(f"   ✅ Completed: {output.get('summary', 'Done')}")

                # Record metric
                self.business.record_metric(
                    'feature_deployed',
                    1,
                    'operational',
                    metadata=decision['action']
                )

            except Exception as e:
                print(f"   ❌ Failed: {e}")
                outputs.append({
                    'success': False,
                    'decision': decision,
                    'error': str(e),
                })

        print(f"\n✅ {len(outputs)} outputs created")
        return outputs

    # Helper methods for autonomous operations

    def _collect_operational_metrics(self) -> Dict:
        """Simulate collecting operational metrics from Shopify/monitoring"""
        # In production, this would call actual APIs
        return {
            'error_rate': 0.008,  # 0.8%
            'avg_response_time': 245,  # ms
            'uptime': 0.998,  # 99.8%
            'api_calls': 1240,
        }

    def _collect_customer_metrics(self) -> Dict:
        """Simulate collecting customer metrics"""
        return {
            'conversion_rate': 0.092,  # 9.2%
            'satisfaction': 4.5,  # out of 5
            'churn_rate': 0.12,  # 12%
            'retention_rate': 0.88,  # 88%
            'nps_score': 42,
        }

    def _collect_financial_metrics(self) -> Dict:
        """Simulate collecting financial metrics"""
        return {
            'revenue': 1240.00,
            'profit_margin': 0.32,  # 32%
            'avg_order_value': 35.50,
            'customer_acquisition_cost': 12.00,
            'lifetime_value': 87.00,
        }

    def _calculate_health_score(self, metrics: Dict) -> int:
        """Calculate overall business health score (0-100)"""
        # Simple weighted average of key metrics
        score = 0
        weights = {
            'conversion_rate': 20,
            'profit_margin': 25,
            'satisfaction': 20,
            'uptime': 15,
            'retention_rate': 20,
        }

        customer = metrics.get('customer', {})
        operational = metrics.get('operational', {})
        financial = metrics.get('financial', {})

        score += customer.get('conversion_rate', 0) / 0.15 * weights['conversion_rate']
        score += financial.get('profit_margin', 0) / 0.30 * weights['profit_margin']
        score += customer.get('satisfaction', 0) / 5.0 * weights['satisfaction']
        score += operational.get('uptime', 0) * weights['uptime']
        score += customer.get('retention_rate', 0) * weights['retention_rate']

        return min(100, int(score))

    def _analyze_customer_patterns(self, customer_data: Dict) -> Dict:
        """Analyze customer data for patterns"""
        patterns = []

        conversion = customer_data.get('conversion_rate', 0)
        if conversion < 0.10:
            patterns.append("Low conversion rate - investigate funnel")
        elif conversion > 0.12:
            patterns.append("Strong conversion - identify what's working")

        satisfaction = customer_data.get('satisfaction', 0)
        if satisfaction < 4.0:
            patterns.append("Below-target satisfaction - review feedback")
        elif satisfaction > 4.5:
            patterns.append("High satisfaction - leverage for testimonials")

        return {
            'patterns': patterns,
            'conversion_trend': 'improving' if conversion > 0.09 else 'needs_work',
            'satisfaction_trend': 'strong' if satisfaction > 4.3 else 'monitor',
        }

    def _analyze_technical_performance(self, operational_data: Dict) -> Dict:
        """Analyze technical performance data"""
        error_rate = operational_data.get('error_rate', 0)
        uptime = operational_data.get('uptime', 1.0)

        return {
            'health': 'good' if error_rate < 0.01 and uptime > 0.99 else 'needs_attention',
            'error_rate_trend': 'low' if error_rate < 0.01 else 'elevated',
            'uptime_trend': 'excellent' if uptime > 0.998 else 'monitor',
        }

    def _identify_opportunities(self, metrics: Dict) -> List[str]:
        """Identify business opportunities from metrics"""
        opportunities = []

        customer = metrics.get('customer', {})
        financial = metrics.get('financial', {})

        # High satisfaction but low conversion = pricing/value prop issue
        if customer.get('satisfaction', 0) > 4.3 and customer.get('conversion_rate', 0) < 0.10:
            opportunities.append("High satisfaction, low conversion - test pricing or messaging")

        # Strong profit margin = room to invest in growth
        if financial.get('profit_margin', 0) > 0.30:
            opportunities.append("Strong margins - invest in customer acquisition")

        # High AOV = upsell opportunity
        if financial.get('avg_order_value', 0) > 30:
            opportunities.append("High AOV - create bundle offers")

        return opportunities

    def _identify_concerns(self, metrics: Dict) -> List[str]:
        """Identify business concerns from metrics"""
        concerns = []

        customer = metrics.get('customer', {})
        operational = metrics.get('operational', {})

        if customer.get('churn_rate', 0) > 0.15:
            concerns.append("Elevated churn rate - investigate retention")

        if operational.get('error_rate', 0) > 0.02:
            concerns.append("Error rate above target - review system health")

        if customer.get('conversion_rate', 0) < 0.08:
            concerns.append("Low conversion rate - urgent funnel optimization needed")

        return concerns

    def _ceo_decide_on_opportunity(self, opportunity: str, insights: Dict) -> Optional[Dict]:
        """CEO decides whether to pursue an opportunity"""
        # Simple decision logic - in production, this would use Claude API
        if "pricing" in opportunity.lower():
            return {
                'action': 'Test $32 price point on new variants',
                'owner': 'CPO',
                'budget': 0,  # No cost to test pricing
                'timeline': '7 days',
                'success_metric': 'conversion_rate',
                'type': 'pricing_test',
            }
        elif "acquisition" in opportunity.lower():
            return {
                'action': 'Launch Instagram ad campaign',
                'owner': 'CPO',
                'budget': 500,
                'timeline': '14 days',
                'success_metric': 'customer_acquisition_cost',
                'type': 'marketing_campaign',
            }
        elif "bundle" in opportunity.lower():
            return {
                'action': 'Create 2-pack bundle offer',
                'owner': 'CPO',
                'budget': 0,
                'timeline': '3 days',
                'success_metric': 'avg_order_value',
                'type': 'product_feature',
            }
        return None

    def _ceo_decide_on_concern(self, concern: str, insights: Dict) -> Optional[Dict]:
        """CEO decides how to address a concern"""
        if "error rate" in concern.lower():
            return {
                'action': 'Investigate and fix error rate spike',
                'owner': 'CTO',
                'budget': 0,
                'timeline': '1 day',
                'success_metric': 'error_rate',
                'type': 'technical_fix',
                'priority': 'high',
            }
        elif "churn" in concern.lower():
            return {
                'action': 'Analyze churn reasons and implement retention campaign',
                'owner': 'CPO',
                'budget': 200,
                'timeline': '10 days',
                'success_metric': 'churn_rate',
                'type': 'retention_initiative',
                'priority': 'high',
            }
        return None

    def _requires_human_approval(self, decision: Dict) -> bool:
        """Check if a decision requires human approval"""
        # Budget over limit
        if decision.get('budget', 0) > self.autonomous_budget_limit:
            decision['reason'] = f"Budget ${decision['budget']} exceeds limit ${self.autonomous_budget_limit}"
            return True

        # Decision type requires approval
        if decision.get('type') in self.require_approval_for:
            decision['reason'] = f"Decision type '{decision['type']}' requires approval"
            return True

        return False

    def _execute_decision(self, decision: Dict) -> Dict:
        """Execute an approved decision"""
        owner = decision.get('owner')
        action = decision.get('action')

        # Route to appropriate agent
        if owner == 'CPO':
            return self._cpo_execute(decision)
        elif owner == 'CTO':
            return self._cto_execute(decision)
        elif owner == 'CEO':
            return self._ceo_execute(decision)
        else:
            raise ValueError(f"Unknown owner: {owner}")

    def _cpo_execute(self, decision: Dict) -> Dict:
        """CPO executes a decision"""
        # Simulate CPO work - in production, this would call actual APIs
        action_type = decision.get('type')

        if action_type == 'pricing_test':
            # Would update Shopify product prices
            return {
                'success': True,
                'summary': f"Updated pricing on 3 variants to test ${decision.get('budget', 0)}",
                'products_updated': 3,
            }
        elif action_type == 'marketing_campaign':
            # Would create and launch marketing campaign
            return {
                'success': True,
                'summary': f"Launched Instagram campaign with ${decision.get('budget', 0)} budget",
                'campaign_id': 'ig_camp_001',
            }
        elif action_type == 'product_feature':
            # Would create new product or feature
            return {
                'success': True,
                'summary': 'Created bundle product in Shopify',
                'product_id': 'bundle_001',
            }

        return {'success': False, 'error': 'Unknown action type'}

    def _cto_execute(self, decision: Dict) -> Dict:
        """CTO executes a decision"""
        action_type = decision.get('type')

        if action_type == 'technical_fix':
            # Would deploy code fix
            return {
                'success': True,
                'summary': 'Deployed fix for error rate spike',
                'error_rate_after': 0.006,
            }

        return {'success': False, 'error': 'Unknown action type'}

    def _ceo_execute(self, decision: Dict) -> Dict:
        """CEO executes a decision"""
        # CEO typically delegates rather than executes
        return {
            'success': True,
            'summary': 'Decision delegated to appropriate agent',
        }

    def print_summary(self):
        """Print summary of loop performance"""
        print("\n" + "=" * 80)
        print("📊 LOOP PERFORMANCE SUMMARY")
        print("=" * 80)
        print(f"Total iterations: {self.loop_metrics.iteration_count}")
        print(f"Successful: {self.loop_metrics.successful_iterations}")
        print(f"Failed: {self.loop_metrics.failed_iterations}")
        print(f"Success rate: {self.loop_metrics.successful_iterations / max(1, self.loop_metrics.iteration_count) * 100:.1f}%")
        print(f"\nAverage cycle time: {self.loop_metrics.avg_cycle_time:.1f}s")
        print(f"\nDecisions made: {self.loop_metrics.decisions_made}")
        print(f"Autonomous: {self.loop_metrics.autonomous_decisions} ({self.loop_metrics.autonomous_decisions / max(1, self.loop_metrics.decisions_made) * 100:.1f}%)")
        print(f"Required approval: {self.loop_metrics.human_approvals_needed}")
        print("=" * 80)


def main():
    """Main entry point for autonomous loop"""
    import argparse

    parser = argparse.ArgumentParser(description='Run The Office autonomous Build-Measure-Learn loop')
    parser.add_argument(
        '--mode',
        choices=['continuous', 'single-cycle', 'demo'],
        default='single-cycle',
        help='Loop execution mode'
    )
    parser.add_argument(
        '--cadence',
        choices=['hourly', 'daily', 'weekly', 'quarterly'],
        default='daily',
        help='Loop cadence (only for continuous mode)'
    )
    parser.add_argument(
        '--budget-limit',
        type=int,
        default=500,
        help='Autonomous budget limit in dollars'
    )

    args = parser.parse_args()

    # Initialize business
    print("🏢 Initializing The Office...")
    business = Business()

    # Create autonomous loop
    cadence_map = {
        'hourly': LoopCadence.HOURLY,
        'daily': LoopCadence.DAILY,
        'weekly': LoopCadence.WEEKLY,
        'quarterly': LoopCadence.QUARTERLY,
    }

    loop = AutonomousLoop(
        business=business,
        cadence=cadence_map[args.cadence],
        autonomous_budget_limit=args.budget_limit,
    )

    # Run based on mode
    if args.mode == 'continuous':
        loop.run_continuous()
    elif args.mode == 'single-cycle':
        result = loop.run_single_cycle()
        loop.print_summary()
        return result
    elif args.mode == 'demo':
        print("\n🎬 DEMO MODE: Running 3 iterations...")
        for i in range(3):
            loop.run_single_cycle()
            if i < 2:
                print("\n⏸️  Waiting 5 seconds before next iteration...\n")
                time.sleep(5)
        loop.print_summary()


if __name__ == "__main__":
    main()

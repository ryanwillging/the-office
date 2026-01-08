"""
Example: Strategic planning with the CEO agent
"""

from src.business import Business


def main():
    business = Business()

    # Record current state
    business.record_metrics({
        'customer': {
            'retention_rate': 0.80,
            'churn_rate': 0.20,
            'conversion_rate': 0.12
        },
        'financial': {
            'profit_margin': 0.25,
            'revenue': 85000
        }
    })

    # Set strategy for next quarter
    print("Setting Q1 2026 Strategy:")
    print("=" * 60)

    strategy = business.set_strategy(
        period="Q1 2026",
        focus_areas=[
            "Reduce customer churn from 20% to 15%",
            "Improve conversion rate to 15%",
            "Increase profit margin to 30%",
            "Launch new product features based on customer feedback"
        ]
    )

    print(strategy)
    print()

    # Make a strategic decision
    print("\nMaking a Strategic Decision:")
    print("=" * 60)

    decision = business.make_decision(
        topic="Should we invest in a mobile app or improve the web experience?",
        context={
            "mobile_traffic": 0.45,
            "web_traffic": 0.55,
            "mobile_conversion": 0.08,
            "web_conversion": 0.15,
            "available_budget": 50000
        }
    )

    print(f"Topic: {decision['topic']}")
    print(f"\nDecision:\n{decision['decision']}")


if __name__ == "__main__":
    main()

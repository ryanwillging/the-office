"""
Example: Product development workflow with CPO and CTO collaboration
"""

from src.business import Business


def main():
    business = Business()

    # CPO designs a new feature based on customer needs
    print("CPO: Designing New Feature")
    print("=" * 60)

    feature_design = business.design_feature(
        feature="Dark mode with automatic switching based on time of day",
        problem="Users complain about eye strain when using the app at night"
    )

    print(f"Feature: {feature_design['feature']}")
    print(f"User Problem: {feature_design['user_problem']}")
    print(f"\nDesign:\n{feature_design['design']}")
    print()

    # Process messages (CTO will respond with technical feasibility)
    print("\nProcessing inter-agent communication...")
    print("=" * 60)
    responses = business.process_all_messages()

    for agent_name, agent_responses in responses.items():
        print(f"\n{agent_name} Responses:")
        for response in agent_responses:
            print(response)
            print()

    # CPO optimizes pricing
    print("\nCPO: Optimizing Pricing Strategy")
    print("=" * 60)

    pricing_analysis = business.cpo.optimize_pricing(
        current_pricing={
            "basic": 9.99,
            "pro": 29.99,
            "enterprise": 99.99
        },
        market_data={
            "competitor_basic": 12.99,
            "competitor_pro": 24.99,
            "our_features_vs_competitors": "More features in basic plan",
            "customer_feedback": "Pricing is fair but enterprise is too expensive"
        }
    )

    print(pricing_analysis)


if __name__ == "__main__":
    main()

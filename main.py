#!/usr/bin/env python3
"""
The Office - AI Business Agent Suite

Main entry point for running the business agent system
"""

import os
from dotenv import load_dotenv
from src.business import Business


def main():
    """Run the business agent suite demo"""

    # Load environment variables
    load_dotenv()

    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY not found in environment variables")
        print("Please copy .env.example to .env and add your API key")
        return

    print("=" * 60)
    print("THE OFFICE - AI Business Agent Suite")
    print("=" * 60)
    print()

    # Initialize the business
    business = Business()

    # Display agent information
    print("Initializing agents...")
    print()
    agent_info = business.get_agent_info()
    for name, info in agent_info.items():
        print(info)
        print("-" * 60)
        print()

    # Example: Record some initial metrics
    print("Recording initial metrics...")
    business.record_metrics({
        'customer': {
            'retention_rate': 0.82,
            'churn_rate': 0.18,
            'conversion_rate': 0.12,
            'satisfaction_score': 4.2
        },
        'operational': {
            'error_rate': 0.03,
            'operational_cost': 15000,
            'efficiency_score': 0.75
        },
        'financial': {
            'profit_margin': 0.28,
            'revenue': 95000,
            'costs': 68400
        }
    })
    print("✓ Metrics recorded")
    print()

    # Example: CEO reviews business status
    print("CEO reviewing business metrics...")
    print()
    review = business.review_business()
    print(review)
    print()
    print("=" * 60)

    # Example: Analyze customer feedback
    print("\nAnalyzing customer feedback...")
    feedback = [
        {"text": "Love the product but the checkout process is confusing", "rating": "4"},
        {"text": "Customer support was very helpful!", "rating": "5"},
        {"text": "The app is slow on mobile", "rating": "3"},
        {"text": "Pricing is too high compared to competitors", "rating": "2"},
        {"text": "Great features, would like more customization options", "rating": "4"}
    ]

    analysis = business.analyze_customer_feedback(feedback)
    print("\nCPO Analysis:")
    print(analysis)
    print()
    print("=" * 60)

    # Show final business status
    print("\nBusiness Status Summary:")
    status = business.get_business_status()
    print(f"Total messages: {status['total_messages']}")
    print(f"Total metrics recorded: {status['total_metrics_recorded']}")
    print()
    print("Current Metrics by Category:")
    for category, metrics in status['metrics'].items():
        if metrics:
            print(f"\n{category.upper()}:")
            for name, value in metrics.items():
                print(f"  {name}: {value}")
    print()
    print("=" * 60)
    print("\nAgent suite initialized and ready!")
    print("Import 'Business' from 'src.business' to use in your code.")


if __name__ == "__main__":
    main()

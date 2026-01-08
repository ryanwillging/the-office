"""
Basic usage example for The Office agent suite
"""

from src.business import Business


def main():
    # Initialize the business with all agents
    business = Business()

    # Record current business metrics
    business.record_metrics({
        'customer': {
            'retention_rate': 0.85,
            'churn_rate': 0.15,
            'conversion_rate': 0.14
        },
        'operational': {
            'error_rate': 0.02,
            'operational_cost': 12000
        },
        'financial': {
            'profit_margin': 0.30,
            'revenue': 100000
        }
    })

    # Get CEO's business review
    print("CEO Business Review:")
    print("=" * 60)
    review = business.review_business()
    print(review)
    print()

    # Analyze customer feedback
    feedback = [
        {"text": "Product is great but needs better mobile support", "rating": "4"},
        {"text": "Customer service responded quickly", "rating": "5"},
        {"text": "Pricing is reasonable", "rating": "4"}
    ]

    print("CPO Customer Feedback Analysis:")
    print("=" * 60)
    analysis = business.analyze_customer_feedback(feedback)
    print(analysis)
    print()

    # Check business status
    status = business.get_business_status()
    print(f"Total messages exchanged: {status['total_messages']}")
    print(f"Metrics tracked: {status['total_metrics_recorded']}")


if __name__ == "__main__":
    main()

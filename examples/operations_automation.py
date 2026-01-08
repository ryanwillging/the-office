"""
Example: Operational automation with the CTO agent
"""

from src.business import Business


def main():
    business = Business()

    # CTO designs an automation
    print("CTO: Designing Automation")
    print("=" * 60)

    automation = business.create_automation(
        task="Daily customer metrics reporting",
        frequency="Daily at 9am",
        process="""
        Current manual process:
        1. Log into analytics dashboard
        2. Export customer data
        3. Calculate retention, churn, conversion rates
        4. Create summary email
        5. Send to CEO and CPO
        6. Update spreadsheet
        """
    )

    print(f"Task: {automation['task']}")
    print(f"Frequency: {automation['frequency']}")
    print(f"\nAutomation Design:\n{automation['automation']}")
    print()

    # CTO designs a new agent
    print("\nCTO: Designing Customer Success Agent")
    print("=" * 60)

    agent_design = business.cto.design_agent(
        goal="Proactively prevent customer churn",
        responsibilities=[
            "Monitor customer engagement metrics",
            "Identify at-risk customers",
            "Trigger automated outreach campaigns",
            "Escalate high-value at-risk customers to human team",
            "Track success of retention interventions"
        ]
    )

    print(f"Goal: {agent_design['goal']}")
    print(f"\nAgent Design:\n{agent_design['design']}")
    print()

    # CTO creates a reusable skill
    print("\nCTO: Creating Reusable Skill")
    print("=" * 60)

    skill = business.cto.create_skill(
        skill_name="CustomerSegmentation",
        purpose="Segment customers based on behavior, value, and risk",
        use_cases=[
            "Identify high-value customers for VIP treatment",
            "Find at-risk customers for retention campaigns",
            "Segment for personalized marketing messages",
            "Analyze product usage patterns by segment"
        ]
    )

    print(f"Skill: {skill['name']}")
    print(f"Purpose: {skill['purpose']}")
    print(f"\nSpecification:\n{skill['specification']}")


if __name__ == "__main__":
    main()

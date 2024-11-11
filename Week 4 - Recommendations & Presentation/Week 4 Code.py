import pandas as pd
import numpy as np


def generate_recommendations(df):
    recommendations = []

    for _, row in df.iterrows():
        profile_id = row["profile_id"]
        engagement_score = row["Engagement Score"]
        days_inactive = row["Days Since Last Engagement"]
        participation_count = row["Opportunity Participation Count"]
        churn = row["Churn"]

        # Initialize a list of recommendations for each student
        student_recommendations = []

        # 1. Personalized Re-engagement Alerts
        if engagement_score < 0.5 or days_inactive > 30:
            student_recommendations.append("Send re-engagement email")

        # 2. Targeted Course Suggestions
        if churn == 1 or participation_count < 1:
            student_recommendations.append(
                "Recommend popular courses based on interests"
            )

        # 3. Incentivize Participation
        if participation_count == 0:
            student_recommendations.append(
                "Offer incentives for first-time participation"
            )

        # Collect recommendations for the student
        recommendations.append(
            {"profile_id": profile_id, "Recommendations": student_recommendations}
        )

    # Convert to DataFrame for better visualization
    recommendations_df = pd.DataFrame(recommendations)
    return recommendations_df


# Usage with the 'students' DataFrame:
recommendations = generate_recommendations(students)
print(recommendations.head())

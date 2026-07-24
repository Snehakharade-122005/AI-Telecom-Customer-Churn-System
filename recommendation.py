def get_recommendation(risk_score):

    if risk_score < 30:
        return {
            "level": "🟢 LOW",
            "message": """
Customer is likely to stay.

Recommendations:
• Continue normal service.
• Send loyalty rewards.
• Maintain customer satisfaction.
"""
        }

    elif risk_score < 70:
        return {
            "level": "🟡 MEDIUM",
            "message": """
Customer has moderate churn risk.

Recommendations:
• Offer personalized discounts.
• Contact customer.
• Improve engagement.
"""
        }

    else:
        return {
            "level": "🔴 HIGH",
            "message": """
Customer is highly likely to churn.

Recommendations:
• Offer annual contract.
• Provide special discount.
• Assign dedicated customer support.
"""
        }
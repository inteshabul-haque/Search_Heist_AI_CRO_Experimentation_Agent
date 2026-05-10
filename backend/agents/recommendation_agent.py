def generate_recommendations(analysis):

    recommendations = []

    analysis_str = str(analysis).lower()

    # Mobile recommendations
    if "mobile" in analysis_str:

        recommendations.append(
            "Optimize mobile checkout experience."
        )

        recommendations.append(
            "Reduce mobile form friction."
        )

    # Funnel recommendations
    if "drop" in analysis_str:

        recommendations.append(
            "Investigate funnel leakage points."
        )

        recommendations.append(
            "Run checkout UX experiments."
        )

    # Experiment recommendations
    if "conversion_rate" in analysis_str:

        recommendations.append(
            "Launch CTA optimization A/B tests."
        )

        recommendations.append(
            "Test simplified checkout flows."
        )

    if len(recommendations) == 0:

        recommendations.append(
            "No major optimization issues detected."
        )

    return recommendations
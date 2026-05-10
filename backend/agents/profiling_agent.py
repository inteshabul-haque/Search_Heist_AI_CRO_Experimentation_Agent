def generate_profile_insights(profile):

    insights = []

    # Missing values
    total_missing = sum(
        profile["missing_values"].values()
    )

    if total_missing > 0:

        insights.append(
            f"Dataset contains {total_missing} missing values."
        )

    # Numeric columns
    numeric_count = len(profile["numeric_columns"])

    insights.append(
        f"Dataset contains {numeric_count} numeric columns."
    )

    # Categorical columns
    categorical_count = len(profile["categorical_columns"])

    insights.append(
        f"Dataset contains {categorical_count} categorical columns."
    )

    # Dataset size
    if profile["rows"] > 100000:

        insights.append(
            "Large dataset detected. Optimized processing recommended."
        )

    if len(insights) == 0:

        insights.append(
            "Dataset quality appears healthy."
        )

    return insights
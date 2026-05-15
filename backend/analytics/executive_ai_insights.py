def generate_executive_insights(

    experiment_results
):

    insights = []

    uplift = experiment_results.get(
        "uplift_percent",
        0
    )

    significant = experiment_results.get(
        "significant",
        False
    )

    winning_variant = experiment_results.get(
        "winning_variant",
        "Unknown"
    )

    conversion_rate = experiment_results.get(
        "winning_conversion_rate",
        0
    )

    # -----------------------------------
    # UPLIFT INSIGHTS
    # -----------------------------------

    if uplift > 15:

        insights.append(
            f"Variant {winning_variant} shows very strong uplift of {uplift}%."
        )

    elif uplift > 5:

        insights.append(
            f"Variant {winning_variant} shows moderate conversion improvement."
        )

    else:

        insights.append(
            "Experiment uplift remains limited."
        )

    # -----------------------------------
    # SIGNIFICANCE
    # -----------------------------------

    if significant:

        insights.append(
            "Experiment reached statistical significance."
        )

    else:

        insights.append(
            "Experiment has not reached statistical significance yet."
        )

    # -----------------------------------
    # CVR QUALITY
    # -----------------------------------

    if conversion_rate > 15:

        insights.append(
            "High conversion efficiency detected."
        )

    elif conversion_rate < 3:

        insights.append(
            "Conversion rate is critically low."
        )

    # -----------------------------------
    # AI TACTICAL
    # -----------------------------------

    insights.append(
        "Recommend segmentation analysis for device and traffic source."
    )

    return insights
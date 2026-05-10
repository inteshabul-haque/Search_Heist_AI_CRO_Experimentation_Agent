def generate_autonomous_insights(results):

    insights = []

    # Funnel Insights
    if "funnel_analysis" in results:

        funnel = results["funnel_analysis"]

        biggest_drop = funnel.get(
            "biggest_drop_stage",
            "unknown"
        )

        drop_count = funnel.get(
            "drop_count",
            0
        )

        insights.append(
            f"Biggest funnel leakage detected at "
            f"{biggest_drop} stage with "
            f"{drop_count} user drop-offs."
        )

    # KPI Insights
    if "kpis" in results:

        kpis = results["kpis"]

        conversion_rate = kpis.get(
            "conversion_rate",
            0
        )

        if conversion_rate < 2:

            insights.append(
                "Critical low conversion rate detected."
            )

        elif conversion_rate < 5:

            insights.append(
                "Moderate conversion performance detected."
            )

        else:

            insights.append(
                "Strong conversion performance detected."
            )

        revenue = kpis.get(
            "total_revenue",
            0
        )

        insights.append(
            f"Total revenue analyzed: {revenue}"
        )

    # Device Insights
    if "device_analysis" in results:

        device_analysis = results["device_analysis"]

        lowest_device = None
        lowest_cr = 999

        for device, values in device_analysis.items():

            cr = values.get(
                "conversion_rate",
                0
            )

            if cr < lowest_cr:

                lowest_cr = cr
                lowest_device = device

        if lowest_device:

            insights.append(
                f"Weakest device performance detected on "
                f"{lowest_device}."
            )

    if len(insights) == 0:

        insights.append(
            "No major risks detected."
        )

    return insights
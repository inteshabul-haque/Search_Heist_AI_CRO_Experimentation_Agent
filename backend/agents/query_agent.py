def process_query(query, analysis):

    query = query.lower()

    # -----------------------------
    # Variant / Winner Detection
    # -----------------------------
    if (
        "variant" in query
        or "winner" in query
        or "best performing" in query
    ):

        experiment_data = analysis.get(
            "experiment_analysis",
            {}
        )

        best_variant = None
        best_cr = 0

        for variant, values in experiment_data.items():

            cr = values.get(
                "conversion_rate",
                0
            )

            if cr > best_cr:

                best_cr = cr
                best_variant = variant

        return (
            f"Best performing variant is "
            f"{best_variant} with "
            f"{best_cr}% conversion rate."
        )

    # -----------------------------
    # Funnel Leakage
    # -----------------------------
    if (
        "funnel" in query
        or "drop" in query
        or "conversion down" in query
        or "most down" in query
        or "where conversion" in query
        or "leakage" in query
    ):

        funnel = analysis.get(
            "funnel_analysis",
            {}
        )

        if funnel:

            stage = funnel.get(
                "biggest_drop_stage",
                "unknown"
            )

            drop_count = funnel.get(
                "drop_count",
                0
            )

            return (
                f"Biggest funnel leakage occurs at "
                f"{stage} with "
                f"{drop_count} user drop-offs."
            )

        # fallback for experiment datasets
        device_data = analysis.get(
            "device_analysis",
            {}
        )

        weakest_device = None
        weakest_cr = 999

        for device, values in device_data.items():

            cr = values.get(
                "conversion_rate",
                0
            )

            if cr < weakest_cr:

                weakest_cr = cr
                weakest_device = device

        if weakest_device:

            return (
                f"Lowest conversion performance detected on "
                f"{weakest_device} with "
                f"{weakest_cr}% conversion rate."
            )

    # -----------------------------
    # Device Performance
    # -----------------------------
    if (
        "device" in query
        or "mobile" in query
        or "desktop" in query
    ):

        device_data = analysis.get(
            "device_analysis",
            {}
        )

        weakest_device = None
        weakest_cr = 999

        for device, values in device_data.items():

            cr = values.get(
                "conversion_rate",
                0
            )

            if cr < weakest_cr:

                weakest_cr = cr
                weakest_device = device

        return (
            f"Weakest device performance detected on "
            f"{weakest_device} with "
            f"{weakest_cr}% conversion rate."
        )

    # -----------------------------
    # Recommendations
    # -----------------------------
    if (
        "optimize" in query
        or "improve" in query
        or "recommendation" in query
    ):

        recommendations = (
            analysis.get("ai_reasoning", {})
            .get("recommendations", [])
        )

        return recommendations

    # -----------------------------
    # Executive Summary
    # -----------------------------
    if (
        "summary" in query
        or "summarize" in query
        or "overview" in query
    ):

        return analysis.get(
            "executive_summary",
            "No summary available."
        )

    return (
        "Unable to determine query intent."
    )
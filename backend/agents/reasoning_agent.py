def generate_reasoning(analysis):

    reasoning = []

    analysis_str = str(analysis).lower()

    if "mobile" in analysis_str:

        reasoning.append(
            "Mobile user behavior indicates possible UX friction."
        )

    if "checkout" in analysis_str:

        reasoning.append(
            "Checkout abandonment suggests funnel inefficiencies."
        )

    if "conversion_rate" in analysis_str:

        reasoning.append(
            "Conversion trends suggest experimentation opportunities."
        )

    if len(reasoning) == 0:

        reasoning.append(
            "No major behavioral issues detected."
        )

    return reasoning
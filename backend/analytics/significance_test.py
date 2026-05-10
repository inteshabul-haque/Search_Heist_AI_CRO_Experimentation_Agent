from scipy.stats import chi2_contingency


def run_significance_test(a_converted, a_total, b_converted, b_total):

    # Create contingency table
    contingency_table = [
        [a_converted, a_total - a_converted],
        [b_converted, b_total - b_converted]
    ]

    # Run chi-square test
    chi2, p_value, _, _ = chi2_contingency(contingency_table)

    # Avoid division by zero
    if a_total == 0 or b_total == 0 or a_converted == 0:
        uplift = 0.0
    else:
        uplift = (
            (
                (b_converted / b_total)
                - (a_converted / a_total)
            )
            / (a_converted / a_total)
        ) * 100

    # Determine significance
    significance = p_value < 0.05

    # Business interpretation
    if significance:
        interpretation = (
            "Variant B shows statistically significant improvement."
        )
    else:
        interpretation = (
            "No statistically significant difference detected."
        )

    return {
        "p_value": round(p_value, 4),
        "significant": significance,
        "uplift_percent": round(uplift, 2),
        "interpretation": interpretation
    }
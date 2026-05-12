from scipy.stats import chi2_contingency

from analytics.uplift_calculator import (
    calculate_uplift
)


# ============================================================
# SIGNIFICANCE TEST
# ============================================================

def run_significance_test(

    a_converted,
    a_total,

    b_converted,
    b_total

):

    # --------------------------------------------------------
    # CONTINGENCY TABLE
    # --------------------------------------------------------

    contingency_table = [

        [

            a_converted,

            a_total - a_converted
        ],

        [

            b_converted,

            b_total - b_converted
        ]
    ]

    # --------------------------------------------------------
    # CHI-SQUARE TEST
    # --------------------------------------------------------

    chi2, p_value, _, _ = (

        chi2_contingency(
            contingency_table
        )
    )

    # --------------------------------------------------------
    # UPLIFT CALCULATION
    # --------------------------------------------------------

    uplift_results = (

        calculate_uplift(

            control_converted=
                a_converted,

            control_total=
                a_total,

            variant_converted=
                b_converted,

            variant_total=
                b_total
        )
    )

    uplift = uplift_results[
        "uplift_percent"
    ]

    control_cr = uplift_results[
        "control_conversion_rate"
    ]

    variant_cr = uplift_results[
        "variant_conversion_rate"
    ]

    # --------------------------------------------------------
    # SIGNIFICANCE LOGIC
    # --------------------------------------------------------

    significance = (
        p_value < 0.05
    )

    confidence_level = (

        round(
            (1 - p_value) * 100,
            2
        )

        if p_value <= 1

        else 0
    )

    # --------------------------------------------------------
    # BUSINESS INTERPRETATION
    # --------------------------------------------------------

    if significance:

        interpretation = (

            f"Variant B shows statistically "
            f"significant improvement with "
            f"{uplift}% uplift and "
            f"{confidence_level}% confidence."
        )

        recommendation = (

            "Recommendation: Consider "
            "rolling out Variant B "
            "to a larger audience."
        )

    else:

        interpretation = (

            "No statistically significant "
            "difference detected between "
            "experiment variants."
        )

        recommendation = (

            "Recommendation: Continue testing "
            "with larger sample size before "
            "making rollout decisions."
        )

    # --------------------------------------------------------
    # RETURN
    # --------------------------------------------------------

    return {

        "p_value":

            float(round(p_value, 4)),

        "confidence_level":

            float(confidence_level),

        "significant":

            bool(significance),

        "control_conversion_rate":

            float(control_cr),

        "variant_conversion_rate":

            float(variant_cr),

        "uplift_percent":

            float(uplift),

        "interpretation":

            str(interpretation),

        "recommendation":

            str(recommendation)
    }
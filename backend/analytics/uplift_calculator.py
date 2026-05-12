# ============================================================
# UPLIFT CALCULATOR
# ============================================================

def calculate_uplift(

    control_converted,
    control_total,

    variant_converted,
    variant_total

):

    # --------------------------------------------------------
    # AVOID DIVISION ERRORS
    # --------------------------------------------------------

    if (

        control_total == 0
        or variant_total == 0
        or control_converted == 0

    ):

        return {

            "control_conversion_rate": 0,

            "variant_conversion_rate": 0,

            "uplift_percent": 0
        }

    # --------------------------------------------------------
    # CONVERSION RATES
    # --------------------------------------------------------

    control_cr = (

        control_converted
        / control_total

    ) * 100

    variant_cr = (

        variant_converted
        / variant_total

    ) * 100

    # --------------------------------------------------------
    # UPLIFT %
    # --------------------------------------------------------

    uplift = (

        (
            variant_cr
            - control_cr
        )

        / control_cr

    ) * 100

    # --------------------------------------------------------
    # RETURN
    # --------------------------------------------------------

    return {

        "control_conversion_rate":

            round(control_cr, 2),

        "variant_conversion_rate":

            round(variant_cr, 2),

        "uplift_percent":

            round(uplift, 2)
    }
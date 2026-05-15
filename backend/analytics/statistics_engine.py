import math

from scipy.stats import norm


# -----------------------------------
# Z TEST
# -----------------------------------

def calculate_z_test(

    control_conversions,
    control_users,

    variant_conversions,
    variant_users
):

    # Conversion rates
    p1 = control_conversions / control_users
    p2 = variant_conversions / variant_users

    # Pooled probability
    pooled = (

        control_conversions +
        variant_conversions

    ) / (

        control_users +
        variant_users
    )

    # Standard error
    se = math.sqrt(

        pooled *

        (1 - pooled) *

        (
            (1 / control_users) +
            (1 / variant_users)
        )
    )

    if se == 0:

        return {
            "z_score": 0,
            "p_value": 1,
            "significant": False
        }

    z = (p2 - p1) / se

    p_value = 2 * (1 - norm.cdf(abs(z)))

    return {

        "z_score": round(z, 4),

        "p_value": round(p_value, 6),

        "significant": p_value < 0.05
    }


# -----------------------------------
# CONFIDENCE INTERVAL
# -----------------------------------

def confidence_interval(

    conversions,
    users,
    confidence=0.95
):

    if users == 0:

        return (0, 0)

    p = conversions / users

    z = norm.ppf(
        1 - ((1 - confidence) / 2)
    )

    se = math.sqrt(
        (p * (1 - p)) / users
    )

    lower = p - (z * se)
    upper = p + (z * se)

    return (
        round(lower * 100, 2),
        round(upper * 100, 2)
    )


# -----------------------------------
# UPLIFT
# -----------------------------------

def calculate_uplift(

    control_rate,
    variant_rate
):

    if control_rate == 0:
        return 0

    uplift = (

        (
            variant_rate -
            control_rate
        )

        / control_rate

    ) * 100

    return round(uplift, 2)
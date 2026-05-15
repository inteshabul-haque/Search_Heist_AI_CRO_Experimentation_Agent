def analyze_funnel_intelligence(funnel_data):

    insights = []

    alerts = []

    visited = funnel_data.get("visited", 0)

    product_view = funnel_data.get(
        "product_view",
        0
    )

    add_to_cart = funnel_data.get(
        "add_to_cart",
        0
    )

    checkout = funnel_data.get(
        "checkout",
        0
    )

    purchase = funnel_data.get(
        "purchase",
        0
    )

    # -----------------------------------
    # STEP CONVERSION RATES
    # -----------------------------------

    pv_rate = (
        (product_view / visited) * 100
        if visited else 0
    )

    atc_rate = (
        (add_to_cart / product_view) * 100
        if product_view else 0
    )

    checkout_rate = (
        (checkout / add_to_cart) * 100
        if add_to_cart else 0
    )

    purchase_rate = (
        (purchase / checkout) * 100
        if checkout else 0
    )

    # -----------------------------------
    # DROP OFFS
    # -----------------------------------

    dropoffs = {

        "visit_to_view":
        visited - product_view,

        "view_to_cart":
        product_view - add_to_cart,

        "cart_to_checkout":
        add_to_cart - checkout,

        "checkout_to_purchase":
        checkout - purchase
    }

    # Largest drop-off
    largest_dropoff = max(
        dropoffs,
        key=dropoffs.get
    )

    # -----------------------------------
    # INSIGHTS
    # -----------------------------------

    insights.append(
        f"Largest funnel drop-off detected at {largest_dropoff.replace('_', ' ')}."
    )

    if atc_rate < 30:

        insights.append(
            "Add-to-cart rate is weak. Product engagement may be low."
        )

    if checkout_rate < 50:

        insights.append(
            "Checkout progression is underperforming."
        )

    if purchase_rate < 40:

        insights.append(
            "Purchase completion rate indicates possible friction during payment."
        )

    # -----------------------------------
    # ALERTS
    # -----------------------------------

    if dropoffs["checkout_to_purchase"] > 200:

        alerts.append({

            "severity": "critical",

            "message":
            "High abandonment detected between checkout and purchase."
        })

    if atc_rate < 20:

        alerts.append({

            "severity": "medium",

            "message":
            "Product pages may lack conversion-driving content."
        })

    # -----------------------------------
    # STEP METRICS
    # -----------------------------------

    step_metrics = {

        "product_view_rate":
        round(pv_rate, 2),

        "add_to_cart_rate":
        round(atc_rate, 2),

        "checkout_rate":
        round(checkout_rate, 2),

        "purchase_rate":
        round(purchase_rate, 2)
    }

    return {

        "insights": insights,

        "alerts": alerts,

        "step_metrics":
        step_metrics,

        "largest_dropoff":
        largest_dropoff
    }
import pandas as pd


# ============================================================
# FUNNEL ANALYSIS
# ============================================================

def analyze_funnel(df):

    # --------------------------------------------------------
    # LOWERCASE COLUMNS
    # --------------------------------------------------------

    df.columns = df.columns.str.lower()

    print(df.columns)

    # --------------------------------------------------------
    # REQUIRED COLUMNS
    # --------------------------------------------------------

    required_columns = [

        "visited",
        "product_view",
        "add_to_cart",
        "checkout",
        "purchase"
    ]

    # --------------------------------------------------------
    # VALIDATE MISSING COLUMNS
    # --------------------------------------------------------

    missing_columns = [

        col for col in required_columns

        if col not in df.columns
    ]

    # --------------------------------------------------------
    # ERROR RESPONSE
    # --------------------------------------------------------

    if missing_columns:

        return {

            "error": True,

            "message":
                "Column names do not match required funnel format.",

            "missing_columns":
                missing_columns,

            "required_columns":
                required_columns
        }

    # --------------------------------------------------------
    # FUNNEL STAGE VALUES
    # --------------------------------------------------------

    visited = int(
        df["visited"].sum()
    )

    product_view = int(
        df["product_view"].sum()
    )

    add_to_cart = int(
        df["add_to_cart"].sum()
    )

    checkout = int(
        df["checkout"].sum()
    )

    purchase = int(
        df["purchase"].sum()
    )

    # --------------------------------------------------------
    # CONVERSION RATE
    # --------------------------------------------------------

    conversion_rate = (

        float(

            round(

                (
                    purchase / visited
                ) * 100,

                2
            )
        )

        if visited > 0

        else 0.0
    )

    # --------------------------------------------------------
    # DROPOFF RATE
    # --------------------------------------------------------

    dropoff_rate = (

        float(

            round(

                100 - conversion_rate,

                2
            )
        )

        if visited > 0

        else 0.0
    )

    # --------------------------------------------------------
    # REVENUE
    # --------------------------------------------------------

    revenue = (

        float(

            round(

                df["revenue"].sum(),

                2
            )
        )

        if "revenue" in df.columns

        else 0.0
    )

    # --------------------------------------------------------
    # AOV
    # --------------------------------------------------------

    avg_order_value = (

        float(

            round(

                revenue / purchase,

                2
            )
        )

        if purchase > 0

        else 0.0
    )

    # --------------------------------------------------------
    # STAGE-WISE DROP-OFF
    # --------------------------------------------------------

    stage_dropoffs = {

        "visit_to_product_view":

            float(

                round(

                    (
                        (
                            visited
                            - product_view
                        )
                        / visited
                    ) * 100,

                    2
                )
            )

            if visited > 0

            else 0.0,

        "product_view_to_cart":

            float(

                round(

                    (
                        (
                            product_view
                            - add_to_cart
                        )
                        / product_view
                    ) * 100,

                    2
                )
            )

            if product_view > 0

            else 0.0,

        "cart_to_checkout":

            float(

                round(

                    (
                        (
                            add_to_cart
                            - checkout
                        )
                        / add_to_cart
                    ) * 100,

                    2
                )
            )

            if add_to_cart > 0

            else 0.0,

        "checkout_to_purchase":

            float(

                round(

                    (
                        (
                            checkout
                            - purchase
                        )
                        / checkout
                    ) * 100,

                    2
                )
            )

            if checkout > 0

            else 0.0
    }

    # --------------------------------------------------------
    # LARGEST DROPOFF
    # --------------------------------------------------------

    largest_dropoff_stage = max(
        stage_dropoffs,
        key=stage_dropoffs.get
    )

    largest_dropoff_value = (
        stage_dropoffs[
            largest_dropoff_stage
        ]
    )

    # --------------------------------------------------------
    # FUNNEL EFFICIENCY
    # --------------------------------------------------------

    funnel_efficiency = (

        float(

            round(

                (
                    purchase / visited
                ) * 100,

                2
            )
        )

        if visited > 0

        else 0.0
    )

    # --------------------------------------------------------
    # RETURN
    # --------------------------------------------------------

    return {

        "kpis": {

            "conversion_rate":
                float(conversion_rate),

            "total_users":
                int(visited),

            "total_revenue":
                float(revenue),

            "avg_order_value":
                float(avg_order_value),

            "funnel_efficiency":
                float(funnel_efficiency)
        },

        "alerts": [

            {

                "severity":
                    "high",

                "message":

                    f"Largest funnel drop-off "
                    f"detected at "
                    f"{largest_dropoff_stage.replace('_', ' ')} "
                    f"with {largest_dropoff_value}% leakage."
            }

        ],

        "stage_dropoffs":

            stage_dropoffs,

        "chart_data": {

            "experiment_chart": {

                "labels": [

                    "Visited",
                    "Product View",
                    "Add To Cart",
                    "Checkout",
                    "Purchase"
                ],

                "values": [

                    int(visited),
                    int(product_view),
                    int(add_to_cart),
                    int(checkout),
                    int(purchase)
                ]
            }
        },

        "recommendations": [

            "Optimize product detail pages to improve add-to-cart engagement.",

            "Reduce checkout friction to minimize lower-funnel abandonment.",

            "Consider retargeting strategies for cart abandoners.",

            "Review mobile funnel experience for usability issues."
        ],

        "autonomous_insights": [

            "Funnel analysis completed successfully.",

            f"Largest funnel leakage detected at "
            f"{largest_dropoff_stage.replace('_', ' ')} "
            f"with {largest_dropoff_value}% drop-off.",

            f"Overall funnel conversion rate is "
            f"{conversion_rate}%",

            f"Average Order Value currently stands at "
            f"${avg_order_value}.",

            "Optimization opportunities identified across funnel stages."
        ],

        "execution_trace": [

            {

                "agent":
                    "Funnel Agent",

                "action":
                    "Calculated funnel stage performance."
            },

            {

                "agent":
                    "Drop-Off Analysis Agent",

                "action":
                    "Detected largest funnel leakage stage."
            },

            {

                "agent":
                    "Revenue Agent",

                "action":
                    "Calculated revenue and AOV metrics."
            },

            {

                "agent":
                    "Insight Agent",

                "action":
                    "Generated autonomous CRO insights."
            }
        ]
    }
import pandas as pd

from analytics.funnel_intelligence import (
    analyze_funnel_intelligence
)

from analytics.device_analysis import (
    analyze_device_segments
)

from utils.json_safe import (
    make_json_safe
)


def analyze_funnel(df):

    # -----------------------------------
    # REQUIRED COLUMNS
    # -----------------------------------

    required_columns = [

        "visited",
        "product_view",
        "add_to_cart",
        "checkout",
        "purchase"
    ]

    for col in required_columns:

        if col not in df.columns:

            return {

                "error":
                f"Missing required column: {col}"
            }

    # -----------------------------------
    # TOTALS
    # -----------------------------------

    visited = int(

        df[
            "visited"
        ].sum()
    )

    product_view = int(

        df[
            "product_view"
        ].sum()
    )

    add_to_cart = int(

        df[
            "add_to_cart"
        ].sum()
    )

    checkout = int(

        df[
            "checkout"
        ].sum()
    )

    purchase = int(

        df[
            "purchase"
        ].sum()
    )

    # -----------------------------------
    # CONVERSION RATE
    # -----------------------------------

    overall_conversion_rate = float(

        round(

            (
                purchase / visited
            ) * 100,

            2
        )

        if visited > 0

        else 0
    )

    # -----------------------------------
    # REVENUE
    # -----------------------------------

    total_revenue = (

        float(

            round(

                df[
                    "revenue"
                ].sum(),

                2
            )
        )

        if "revenue" in df.columns

        else "N/A"
    )

    avg_order_value = (

        float(

            round(

                df[
                    "revenue"
                ].sum()

                / purchase,

                2
            )
        )

        if (
            "revenue" in df.columns
            and purchase > 0
        )

        else "N/A"
    )

    # -----------------------------------
    # FUNNEL DATA
    # -----------------------------------

    funnel_data = {

        "visited":
        int(visited),

        "product_view":
        int(product_view),

        "add_to_cart":
        int(add_to_cart),

        "checkout":
        int(checkout),

        "purchase":
        int(purchase)
    }

    # -----------------------------------
    # DEVICE SEGMENTS
    # -----------------------------------

    device_segments = analyze_device_segments(
        df
    )

    # -----------------------------------
    # FUNNEL INTELLIGENCE
    # -----------------------------------

    intelligence = analyze_funnel_intelligence(
        funnel_data
    )

    # -----------------------------------
    # EXECUTION TRACE
    # -----------------------------------

    execution_trace = [

        {
            "agent":
            "Funnel Analyzer",

            "action":
            "Processed funnel stage metrics."
        },

        {
            "agent":
            "Dropoff Intelligence",

            "action":
            f"Detected largest drop-off at {intelligence['largest_dropoff']}."
        },

        {
            "agent":
            "Tactical Recommendation Engine",

            "action":
            "Generated funnel optimization insights."
        }
    ]

    # -----------------------------------
    # FINAL RESPONSE
    # -----------------------------------

    response = {

        "kpis": {

            "conversion_rate":
            float(
                overall_conversion_rate
            ),

            "total_users":
            int(visited),

            "total_revenue":
            total_revenue,

            "avg_order_value":
            avg_order_value
        },

        "funnel_data":
        funnel_data,

        "device_segments":
        device_segments,

        "step_metrics":
        intelligence[
            "step_metrics"
        ],

        "alerts":
        intelligence[
            "alerts"
        ],

        "autonomous_insights":
        intelligence[
            "insights"
        ],

        "execution_trace":
        execution_trace
    }

    return make_json_safe(response)
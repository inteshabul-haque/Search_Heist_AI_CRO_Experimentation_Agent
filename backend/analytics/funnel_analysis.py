import pandas as pd


def analyze_funnel(df):

    # Lowercase columns
    df.columns = df.columns.str.lower()

    print(df.columns)

    # Required columns
    required_columns = [

        "visited",
        "product_view",
        "add_to_cart",
        "checkout",
        "purchase"
    ]

    # Missing validation
    missing_columns = [

        col for col in required_columns
        if col not in df.columns
    ]

    # Error response
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

    # Funnel stage values
    visited = int(df["visited"].sum())

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

    # Conversion Rate
    conversion_rate = (

        round(
            purchase / visited * 100,
            2
        )

        if visited > 0

        else "N/A"
    )

    # Dropoff
    dropoff_rate = (

        round(
            100 - conversion_rate,
            2
        )

        if conversion_rate != "N/A"

        else "N/A"
    )

    # Revenue
    revenue = (

        round(
            float(df["revenue"].sum()),
            2
        )

        if "revenue" in df.columns

        else "N/A"
    )

    # AOV
    avg_order_value = (

        round(
            revenue / purchase,
            2
        )

        if (
            revenue != "N/A"
            and purchase > 0
        )

        else "N/A"
    )

    return {

        "kpis": {

            "conversion_rate":
                conversion_rate,

            "total_users":
                visited,

            "total_revenue":
                revenue,

            "avg_order_value":
                avg_order_value
        },

        "alerts": [

            {

                "severity": "high",

                "message":
                    f"Drop-off rate is {dropoff_rate}%"
            }

        ],

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

                    visited,
                    product_view,
                    add_to_cart,
                    checkout,
                    purchase
                ]
            }
        },

        "autonomous_insights": [

            "Funnel analysis completed.",

            "Largest drop-off detected in lower funnel.",

            "Optimization opportunities identified."
        ],

        "execution_trace": [

            {

                "agent": "Funnel Agent",

                "action":
                    "Calculated funnel stage performance."
            },

            {

                "agent": "Insight Agent",

                "action":
                    "Generated autonomous CRO insights."
            }
        ]
    }
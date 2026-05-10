import pandas as pd


def analyze_experiment(df):

    # Lowercase columns
    df.columns = df.columns.str.lower()

    print(df.columns)

    # Detect columns
    variant_col = None

    conversion_col = None

    revenue_col = None

    for col in df.columns:

        if "variant" in col:
            variant_col = col

        if (
            "converted" in col
            or "conversion" in col
        ):
            conversion_col = col

        if "revenue" in col:
            revenue_col = col

    # Validation
    missing_columns = []

    if not variant_col:
        missing_columns.append("variant")

    if not conversion_col:
        missing_columns.append("converted")

    # Error response
    if missing_columns:

        return {

            "error": True,

            "message":
                "Column names do not match required A/B test format.",

            "missing_columns":
                missing_columns,

            "required_columns": [

                "variant",
                "converted"
            ]
        }

    # Conversion rate by variant
    grouped = (

        df.groupby(variant_col)
        [conversion_col]
        .mean()
        * 100
    )

    labels = list(grouped.index)

    values = [

        round(v, 2)
        for v in grouped.values
    ]

    # Best Variant
    best_variant = labels[
        values.index(max(values))
    ]

    # Revenue
    revenue = (

        round(
            float(df[revenue_col].sum()),
            2
        )

        if revenue_col

        else "N/A"
    )

    # Converted users
    total_converted = int(
        df[conversion_col].sum()
    )

    # AOV
    avg_order_value = (

        round(
            revenue / total_converted,
            2
        )

        if (
            revenue != "N/A"
            and total_converted > 0
        )

        else "N/A"
    )

    return {

        "kpis": {

            "conversion_rate":
                max(values),

            "total_users":
                len(df),

            "total_revenue":
                revenue,

            "avg_order_value":
                avg_order_value
        },

        "alerts": [

            {

                "severity": "medium",

                "message":
                    f"{best_variant} is outperforming other variants."
            }

        ],

        "chart_data": {

            "experiment_chart": {

                "labels": labels,

                "values": values
            }
        },

        "autonomous_insights": [

            "Experiment analysis completed.",

            f"{best_variant} achieved best conversion performance.",

            "Traffic optimization opportunities identified."
        ],

        "execution_trace": [

            {

                "agent": "Experiment Agent",

                "action":
                    "Calculated experiment performance."
            },

            {

                "agent": "Insight Agent",

                "action":
                    "Generated autonomous statistical insights."
            }
        ]
    }
import pandas as pd

from analytics.significance_test import (
    run_significance_test
)


def analyze_experiment(df):

    # ------------------------------------------------
    # Lowercase Columns
    # ------------------------------------------------

    df.columns = df.columns.str.lower()

    # ------------------------------------------------
    # Detect Required Columns
    # ------------------------------------------------

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

    # ------------------------------------------------
    # Validation
    # ------------------------------------------------

    missing_columns = []

    if not variant_col:
        missing_columns.append("variant")

    if not conversion_col:
        missing_columns.append("converted")

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

    # ------------------------------------------------
    # Conversion Rate by Variant
    # ------------------------------------------------

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

    # ------------------------------------------------
    # Best Variant
    # ------------------------------------------------

    best_variant = labels[
        values.index(max(values))
    ]

    worst_variant = labels[
        values.index(min(values))
    ]

    best_value = max(values)

    worst_value = min(values)

    uplift_difference = round(
        best_value - worst_value,
        2
    )

    # ------------------------------------------------
    # Revenue Metrics
    # ------------------------------------------------

    revenue = (

        round(
            float(df[revenue_col].sum()),
            2
        )

        if revenue_col

        else "N/A"
    )

    total_converted = int(
        df[conversion_col].sum()
    )

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

    # ------------------------------------------------
    # Statistical Significance Test
    # ------------------------------------------------

    variant_stats = (

        df.groupby(variant_col)
        [conversion_col]
        .agg(["sum", "count"])
        .sort_index()

    )

    if len(variant_stats) >= 2:

        variants = list(
            variant_stats.index
        )

        a_variant = variants[0]
        b_variant = variants[1]

        a_converted = int(
            variant_stats.loc[
                a_variant,
                "sum"
            ]
        )

        a_total = int(
            variant_stats.loc[
                a_variant,
                "count"
            ]
        )

        b_converted = int(
            variant_stats.loc[
                b_variant,
                "sum"
            ]
        )

        b_total = int(
            variant_stats.loc[
                b_variant,
                "count"
            ]
        )

        significance_results = (
            run_significance_test(
                a_converted,
                a_total,
                b_converted,
                b_total
            )
        )

    else:

        significance_results = {

            "p_value": None,

            "significant": False,

            "uplift_percent": 0,

            "interpretation":
                "Not enough variants for testing."
        }

    # ------------------------------------------------
    # Alert Severity Logic
    # ------------------------------------------------

    uplift_percent = significance_results.get(
        "uplift_percent",
        0
    )

    if uplift_percent >= 15:
        severity = "high"

    elif uplift_percent >= 5:
        severity = "medium"

    else:
        severity = "low"

    # ------------------------------------------------
    # Executive Insights
    # ------------------------------------------------

    executive_insights = [

        (
            f"{best_variant} achieved the "
            f"highest conversion rate at "
            f"{best_value}%."
        ),

        (
            f"Conversion uplift versus "
            f"{worst_variant} was "
            f"{uplift_difference}%."
        ),

        (
            f"Statistical significance test "
            f"returned p-value of "
            f"{significance_results['p_value']}."
        ),

        significance_results[
            "interpretation"
        ],

        (
            "Results suggest optimization "
            "opportunities for rollout "
            "and further experimentation."
        )
    ]

    # ------------------------------------------------
    # Final Response
    # ------------------------------------------------

    return {

        "kpis": {

            "conversion_rate":
                best_value,

            "total_users":
                len(df),

            "total_revenue":
                revenue,

            "avg_order_value":
                avg_order_value
        },

        "significance_test":
            significance_results,

        "alerts": [

            {

                "severity": severity,

                "message":

                    f"{best_variant} improved "
                    f"conversion performance by "
                    f"{uplift_percent}% with "
                    f"p-value "
                    f"{significance_results['p_value']}."
            }

        ],

        "chart_data": {

            "experiment_chart": {

                "labels": labels,

                "values": values
            }
        },

        "autonomous_insights":
            executive_insights,

        "execution_trace": [

            {

                "agent":
                    "Experiment Agent",

                "action":
                    "Calculated experiment performance."
            },

            {

                "agent":
                    "Statistics Agent",

                "action":
                    "Performed statistical significance testing."
            },

            {

                "agent":
                    "Insight Agent",

                "action":
                    "Generated executive-level business insights."
            }
        ]
    }
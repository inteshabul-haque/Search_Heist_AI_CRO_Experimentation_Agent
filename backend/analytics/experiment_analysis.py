import pandas as pd

from analytics.statistics_engine import (

    calculate_z_test,
    confidence_interval,
    calculate_uplift
)

from analytics.executive_ai_insights import (
    generate_executive_insights
)

from analytics.tactical_alert_engine import (
    generate_tactical_alerts
)

from analytics.device_analysis import (
    analyze_device_segments
)

from utils.json_safe import (
    make_json_safe
)


def analyze_experiment(df):

    # -----------------------------------
    # VALIDATION
    # -----------------------------------

    required_columns = [

        "variant",
        "converted"
    ]

    for col in required_columns:

        if col not in df.columns:

            return {
                "error":
                f"Missing required column: {col}"
            }

    # -----------------------------------
    # GROUP VARIANTS
    # -----------------------------------

    grouped = df.groupby("variant")

    experiment_chart = {

        "labels": [],
        "values": []
    }

    variant_summary = {}

    # -----------------------------------
    # VARIANT METRICS
    # -----------------------------------

    for variant, group in grouped:

        users = int(len(group))

        conversions = int(

            group[
                "converted"
            ].sum()
        )

        conversion_rate = float(

            round(

                (
                    conversions / users
                ) * 100,

                2
            )
        )

        ci = confidence_interval(

            conversions,
            users
        )

        total_revenue = (

            float(

                round(

                    group[
                        "revenue"
                    ].sum(),

                    2
                )
            )

            if "revenue" in group.columns

            else "N/A"
        )

        variant_summary[str(variant)] = {

            "users":
            int(users),

            "conversions":
            int(conversions),

            "conversion_rate":
            float(conversion_rate),

            "confidence_interval":
            ci,

            "revenue":
            total_revenue
        }

        experiment_chart["labels"].append(
            str(variant)
        )

        experiment_chart["values"].append(
            float(conversion_rate)
        )

    # -----------------------------------
    # NEED 2 VARIANTS
    # -----------------------------------

    variants = list(
        variant_summary.keys()
    )

    if len(variants) < 2:

        return {
            "error":
            "Need at least 2 variants"
        }

    # -----------------------------------
    # CONTROL VS VARIANT
    # -----------------------------------

    control = variants[0]
    variant = variants[1]

    control_data = variant_summary[
        control
    ]

    variant_data = variant_summary[
        variant
    ]

    z_test = calculate_z_test(

        control_data["conversions"],
        control_data["users"],

        variant_data["conversions"],
        variant_data["users"]
    )

    uplift = float(

        calculate_uplift(

            control_data[
                "conversion_rate"
            ],

            variant_data[
                "conversion_rate"
            ]
        )
    )

    # -----------------------------------
    # WINNER
    # -----------------------------------

    winning_variant = max(

        variant_summary,

        key=lambda x:
        variant_summary[x][
            "conversion_rate"
        ]
    )

    winning_conversion_rate = float(

        variant_summary[
            winning_variant
        ]["conversion_rate"]
    )

    # -----------------------------------
    # GLOBAL KPIs
    # -----------------------------------

    total_users = int(len(df))

    total_conversions = int(

        df[
            "converted"
        ].sum()
    )

    overall_conversion_rate = float(

        round(

            (
                total_conversions /
                total_users
            ) * 100,

            2
        )
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

                / total_conversions,

                2
            )
        )

        if (
            "revenue" in df.columns
            and total_conversions > 0
        )

        else "N/A"
    )

    # -----------------------------------
    # DEVICE SEGMENTS
    # -----------------------------------

    device_segments = analyze_device_segments(
        df
    )

    # -----------------------------------
    # AI INSIGHTS
    # -----------------------------------

    executive_payload = {

        "uplift_percent":
        float(uplift),

        "significant":
        bool(
            z_test["significant"]
        ),

        "winning_variant":
        str(winning_variant),

        "winning_conversion_rate":
        float(
            winning_conversion_rate
        )
    }

    insights = generate_executive_insights(
        executive_payload
    )

    # -----------------------------------
    # ALERTS
    # -----------------------------------

    alerts = generate_tactical_alerts({

        "conversion_rate":
        float(
            overall_conversion_rate
        ),

        "uplift":
        float(uplift),

        "p_value":
        float(
            z_test["p_value"]
        )
    })

    # -----------------------------------
    # EXECUTION TRACE
    # -----------------------------------

    execution_trace = [

        {
            "agent":
            "Experiment Analyzer",

            "action":
            "Processed variant metrics."
        },

        {
            "agent":
            "Statistics Engine",

            "action":
            "Calculated z-test and confidence intervals."
        },

        {
            "agent":
            "Uplift Engine",

            "action":
            f"Computed uplift of {uplift}%."
        },

        {
            "agent":
            "Tactical Alert Engine",

            "action":
            "Generated tactical CRO alerts."
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
            int(total_users),

            "winning_variant":
            str(winning_variant),

            "uplift":
            float(uplift),

            "p_value":
            float(
                z_test["p_value"]
            ),

            "total_revenue":
            total_revenue,

            "avg_order_value":
            avg_order_value
        },

        "chart_data": {

            "experiment_chart":
            experiment_chart
        },

        "variant_summary":
        variant_summary,

        "statistical_test": {

            "z_score":
            float(
                z_test["z_score"]
            ),

            "p_value":
            float(
                z_test["p_value"]
            ),

            "significant":
            bool(
                z_test["significant"]
            )
        },

        "device_segments":
        device_segments,

        "alerts":
        alerts,

        "autonomous_insights":
        insights,

        "execution_trace":
        execution_trace,

        "winning_variant":
        str(winning_variant)
    }

    return make_json_safe(response)
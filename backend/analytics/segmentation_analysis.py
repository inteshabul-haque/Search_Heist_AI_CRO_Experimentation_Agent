import pandas as pd


# ============================================================
# SEGMENTATION ANALYSIS
# ============================================================

def analyze_segments(df):

    # --------------------------------------------------------
    # LOWERCASE COLUMNS
    # --------------------------------------------------------

    df.columns = df.columns.str.lower()

    insights = []

    segment_results = {}

    # --------------------------------------------------------
    # POSSIBLE SEGMENT COLUMNS
    # --------------------------------------------------------

    segment_columns = [

        "device",
        "country",
        "gender",
        "channel",
        "source",
        "campaign",
        "segment",
        "audience"
    ]

    # --------------------------------------------------------
    # CHECK EACH SEGMENT
    # --------------------------------------------------------

    for col in segment_columns:

        if col in df.columns:

            grouped = (

                df.groupby(col)
                .agg({

                    "converted": "sum",

                    "revenue": "sum"
                    if "revenue" in df.columns
                    else "count"
                })
            )

            grouped["users"] = (
                df.groupby(col).size()
            )

            grouped["conversion_rate"] = (

                grouped["converted"]
                / grouped["users"]
            ) * 100

            grouped = grouped.sort_values(

                by="conversion_rate",

                ascending=False
            )

            # ------------------------------------------------
            # BEST SEGMENT
            # ------------------------------------------------

            best_segment = grouped.index[0]

            best_cr = round(

                grouped.iloc[0]
                ["conversion_rate"],

                2
            )

            best_users = int(

                grouped.iloc[0]
                ["users"]
            )

            best_revenue = round(

                grouped.iloc[0]
                ["revenue"],

                2
            )

            # ------------------------------------------------
            # SAVE RESULTS
            # ------------------------------------------------

            segment_results[col] = (

                grouped.reset_index()
                .to_dict(
                    orient="records"
                )
            )

            # ------------------------------------------------
            # GENERATE INSIGHT
            # ------------------------------------------------

            insights.append(

                f"{best_segment} users "
                f"within {col} delivered the "
                f"highest conversion rate at "
                f"{best_cr}% across "
                f"{best_users} users, generating "
                f"${best_revenue} in revenue."
            )

    # --------------------------------------------------------
    # FALLBACK
    # --------------------------------------------------------

    if not insights:

        insights.append(

            "No segmentation columns were detected in the dataset."
        )

    # --------------------------------------------------------
    # RETURN
    # --------------------------------------------------------

    return {

        "segment_insights": insights,

        "segment_results": segment_results
    }
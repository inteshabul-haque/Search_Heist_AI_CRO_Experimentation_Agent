# ============================================================
# GLOBAL MEMORY
# ============================================================

LATEST_RESULTS = {}


# ============================================================
# SAVE RESULTS
# ============================================================

def save_results(results):

    global LATEST_RESULTS

    LATEST_RESULTS = results


# ============================================================
# MASTER AGENT
# ============================================================

def run_master_agent(question):

    global LATEST_RESULTS

    question = question.lower()

    # --------------------------------------------------------
    # NO DATA
    # --------------------------------------------------------

    if not LATEST_RESULTS:

        return {

            "answer":
                "No dataset analyzed yet. Upload a dataset first."
        }

    # --------------------------------------------------------
    # EXTRACT RESULTS
    # --------------------------------------------------------

    kpis = LATEST_RESULTS.get(
        "kpis",
        {}
    )

    alerts = LATEST_RESULTS.get(
        "alerts",
        []
    )

    insights = LATEST_RESULTS.get(
        "autonomous_insights",
        []
    )

    significance = LATEST_RESULTS.get(
        "significance_test",
        {}
    )

    segmentation = LATEST_RESULTS.get(
        "segmentation_analysis",
        {}
    )

    segment_insights = segmentation.get(
        "segment_insights",
        []
    )

    execution_trace = LATEST_RESULTS.get(
        "execution_trace",
        []
    )

    # --------------------------------------------------------
    # CONVERSION RATE
    # --------------------------------------------------------

    if "conversion" in question:

        uplift = significance.get(
            "uplift_percent",
            "N/A"
        )

        return {

            "answer":

                f"Current conversion rate is "
                f"{kpis.get('conversion_rate', 'N/A')}%. "
                f"Experiment uplift observed: "
                f"{uplift}%."
        }

    # --------------------------------------------------------
    # USERS
    # --------------------------------------------------------

    elif (

        "how many user" in question
        or "total user" in question
        or "users" in question

    ):

        return {

            "answer":

                f"Total users analyzed: "
                f"{kpis.get('total_users', 'N/A')}."
        }

    # --------------------------------------------------------
    # REVENUE
    # --------------------------------------------------------

    elif (

        "revenue" in question
        or "sales" in question

    ):

        return {

            "answer":

                f"Total revenue generated: "
                f"${kpis.get('total_revenue', 'N/A')}."
        }

    # --------------------------------------------------------
    # AOV
    # --------------------------------------------------------

    elif (

        "aov" in question
        or "avg order value" in question
        or "average order value" in question

    ):

        return {

            "answer":

                f"Average Order Value (AOV) "
                f"is ${kpis.get('avg_order_value', 'N/A')}."
        }

    # --------------------------------------------------------
    # SIGNIFICANCE TEST
    # --------------------------------------------------------

    elif (

        "significance" in question
        or "confidence" in question
        or "p value" in question
        or "uplift" in question

    ):

        return {

            "answer":

                f"P-value: "
                f"{significance.get('p_value', 'N/A')}. "

                f"Uplift observed: "
                f"{significance.get('uplift_percent', 'N/A')}%. "

                f"{significance.get('interpretation', '')}"
        }

    # --------------------------------------------------------
    # ALERTS
    # --------------------------------------------------------

    elif (

        "alert" in question
        or "issue" in question
        or "problem" in question
        or "risk" in question

    ):

        if alerts:

            return {

                "answer":

                    alerts[0]["message"]
            }

        return {

            "answer":
                "No major alerts detected."
        }

    # --------------------------------------------------------
    # SEGMENTATION
    # --------------------------------------------------------

    elif (

        "segment" in question
        or "audience" in question
        or "device" in question
        or "channel" in question
        or "customer type" in question

    ):

        if segment_insights:

            return {

                "answer":

                    "\n".join(
                        segment_insights
                    )
            }

        return {

            "answer":
                "No segmentation insights available."
        }

    # --------------------------------------------------------
    # INSIGHTS
    # --------------------------------------------------------

    elif (

        "insight" in question
        or "summary" in question
        or "analysis" in question

    ):

        if insights:

            return {

                "answer":

                    "\n".join(
                        insights
                    )
            }

        return {

            "answer":
                "No insights available."
        }

    # --------------------------------------------------------
    # EXECUTION TRACE
    # --------------------------------------------------------

    elif (

        "trace" in question
        or "workflow" in question
        or "agent" in question

    ):

        if execution_trace:

            formatted_trace = [

                f"{step['agent']} → "
                f"{step['action']}"

                for step in execution_trace
            ]

            return {

                "answer":

                    "\n".join(
                        formatted_trace
                    )
            }

        return {

            "answer":
                "No execution trace available."
        }

    # --------------------------------------------------------
    # GREETING
    # --------------------------------------------------------

    elif (

        "hi" in question
        or "hello" in question

    ):

        return {

            "answer":
                """
Professor online.

Ask me about:
- conversion rate
- users
- revenue
- alerts
- insights
- segmentation
- significance test
- uplift
- funnel drop-offs
- experiment performance
- execution trace
"""
        }

    # --------------------------------------------------------
    # DEFAULT
    # --------------------------------------------------------

    else:

        return {

            "answer":
                """
AI analyzed the latest uploaded dataset successfully.

You can ask about:
- conversion rate
- revenue
- AOV
- significance test
- uplift %
- segmentation
- customer behavior
- device performance
- alerts
- insights
- experiment analysis
- funnel issues
- execution trace
"""
        }
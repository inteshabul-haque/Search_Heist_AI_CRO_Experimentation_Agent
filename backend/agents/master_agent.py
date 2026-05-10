# Global memory
LATEST_RESULTS = {}


def save_results(results):

    global LATEST_RESULTS

    LATEST_RESULTS = results


def run_master_agent(question):

    global LATEST_RESULTS

    question = question.lower()

    # No dataset uploaded
    if not LATEST_RESULTS:

        return {

            "answer":
                "No dataset analyzed yet. Upload a dataset first."
        }

    # Extract data
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

    # Conversion Rate
    if (
        "conversion" in question
    ):

        return {

            "answer":
                f"Current conversion rate is {kpis.get('conversion_rate', 'N/A')}%."
        }

    # Users
    elif (
        "how many user" in question
        or "total user" in question
        or "users" in question
    ):

        return {

            "answer":
                f"Total users are {kpis.get('total_users', 'N/A')}."
        }

    # Revenue
    elif (
        "revenue" in question
        or "sales" in question
    ):

        return {

            "answer":
                f"Total revenue is {kpis.get('total_revenue', 'N/A')}."
        }

    # AOV
    elif (
        "aov" in question
        or "avg order value" in question
    ):

        return {

            "answer":
                f"Average Order Value is {kpis.get('avg_order_value', 'N/A')}."
        }

    # Alerts
    elif (
        "alert" in question
        or "issue" in question
        or "problem" in question
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

    # Insights
    elif (
        "insight" in question
        or "summary" in question
    ):

        if insights:

            return {

                "answer":
                    "\n".join(insights)
            }

        return {

            "answer":
                "No insights available."
        }

    # Greeting
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
- experiment performance
- funnel drop-offs
"""
        }

    # Default
    else:

        return {

            "answer":
                """
AI analyzed the latest uploaded dataset successfully.

You can ask:
- conversion rate
- total users
- revenue
- alerts
- insights
- AOV
- funnel issues
- experiment insights
"""
        }
def planner_agent(user_query):

    query = user_query.lower()

    if "funnel" in query:
        return "funnel_analysis"

    elif "experiment" in query:
        return "experiment_analysis"

    elif "ab test" in query:
        return "experiment_analysis"

    return "general_analysis"
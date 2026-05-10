def route_request(user_query):

    query = user_query.lower()

    if "funnel" in query:
        return "funnel"

    if "experiment" in query:
        return "experiment"

    if "significance" in query:
        return "significance"

    if "mobile" in query:
        return "device"

    return "general"
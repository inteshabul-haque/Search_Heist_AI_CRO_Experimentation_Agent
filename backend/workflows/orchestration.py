from agents.router_agent import route_request


def orchestrate(user_query):

    route = route_request(user_query)

    return {
        "query": user_query,
        "route": route
    }
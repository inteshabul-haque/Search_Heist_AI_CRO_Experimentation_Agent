chat_history = []

latest_analysis = {}


def save_message(role, message):

    chat_history.append({
        "role": role,
        "message": message
    })


def get_chat_history():

    return chat_history


def save_analysis(results):

    global latest_analysis

    latest_analysis = results


def get_latest_analysis():

    return latest_analysis
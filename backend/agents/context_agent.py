from memory.chat_memory import get_latest_analysis


def build_context():

    analysis = get_latest_analysis()

    if not analysis:
        return "No dataset analysis available."

    return f"""
    Latest Analysis Context:

    {analysis}
    """
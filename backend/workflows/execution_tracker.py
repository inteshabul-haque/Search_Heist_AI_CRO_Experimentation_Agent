execution_log = []


def log_agent_step(agent_name, action):

    execution_log.append({
        "agent": agent_name,
        "action": action
    })


def get_execution_log():

    return execution_log


def clear_execution_log():

    global execution_log

    execution_log = []
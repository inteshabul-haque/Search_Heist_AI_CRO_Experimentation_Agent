workflow_state = {
    "current_stage": None,
    "completed_agents": [],
    "shared_context": {},
    "status": "idle"
}


def initialize_workflow():

    global workflow_state

    workflow_state = {
        "current_stage": "initialized",
        "completed_agents": [],
        "shared_context": {},
        "status": "running"
    }


def update_stage(stage_name):

    workflow_state["current_stage"] = stage_name


def complete_agent(agent_name):

    workflow_state["completed_agents"].append(
        agent_name
    )


def update_context(key, value):

    workflow_state["shared_context"][key] = value


def finalize_workflow():

    workflow_state["status"] = "completed"


def get_workflow_state():

    return workflow_state
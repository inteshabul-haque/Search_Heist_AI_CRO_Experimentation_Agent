from agents.reasoning_agent import generate_reasoning
from agents.recommendation_agent import generate_recommendations


def run_ai_workflow(analysis):

    reasoning = generate_reasoning(analysis)

    recommendations = generate_recommendations(analysis)

    return {
        "reasoning": reasoning,
        "recommendations": recommendations
    }

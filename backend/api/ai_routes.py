from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import pandas as pd

from analytics.funnel_analysis import (
    analyze_funnel
)

from analytics.experiment_analysis import (
    analyze_experiment
)

from agents.master_agent import (
    run_master_agent,
    save_results
)

from pydantic import BaseModel

router = APIRouter()


# -------------------------------
# ASK AI MODEL
# -------------------------------

class QuestionRequest(BaseModel):

    question: str


# -------------------------------
# HOME
# -------------------------------

@router.get("/")

def home():

    return {

        "message":
            "Search Heist AI Backend Running"
    }


# -------------------------------
# HEALTH
# -------------------------------

@router.get("/health")

def health():

    return {

        "status":
            "healthy"
    }


# -------------------------------
# FUNNEL ANALYSIS
# -------------------------------

@router.post("/upload-funnel")

async def upload_funnel(

    file: UploadFile = File(...)
):

    try:

        # Read CSV
        df = pd.read_csv(file.file)

        # Analyze
        results = analyze_funnel(df)

        # Save to AI memory
        save_results(results)

        return results

    except Exception as e:

        return {

            "error": True,

            "message":
                str(e)
        }


# -------------------------------
# EXPERIMENT ANALYSIS
# -------------------------------

@router.post("/upload-experiment")

async def upload_experiment(

    file: UploadFile = File(...)
):

    try:

        # Read CSV
        df = pd.read_csv(file.file)

        # Analyze
        results = analyze_experiment(df)

        # Save to AI memory
        save_results(results)

        return results

    except Exception as e:

        return {

            "error": True,

            "message":
                str(e)
        }


# -------------------------------
# ASK AI
# -------------------------------

@router.post("/ask-ai")

async def ask_ai(

    request: QuestionRequest
):

    try:

        result = run_master_agent(
            request.question
        )

        return result

    except Exception as e:

        return {

            "answer":
                f"AI Error: {str(e)}"
        }
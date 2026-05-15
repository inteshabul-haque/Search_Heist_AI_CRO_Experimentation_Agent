import os
import pandas as pd
import google.generativeai as genai

from dotenv import load_dotenv

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from pydantic import BaseModel

from prompts.experiment_prompts import build_experiment_prompt

from analytics.funnel_analysis import analyze_funnel
from analytics.experiment_analysis import analyze_experiment
from analytics.segmentation_analysis import analyze_segments
from analytics.device_analysis import analyze_device_performance

from agents.master_agent import save_results


# ====================================================
# LOAD ENV VARIABLES
# ====================================================

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

router = APIRouter()


# ====================================================
# SAVE DATASET
# ====================================================

def save_latest_dataset(df):

    os.makedirs(
        "datasets",
        exist_ok=True
    )

    dataset_path = (
        "datasets/latest_uploaded_file.csv"
    )

    df.to_csv(
        dataset_path,
        index=False
    )


# ====================================================
# REQUEST MODEL
# ====================================================

class QuestionRequest(BaseModel):

    question: str


# ====================================================
# HOME
# ====================================================

@router.get("/")

def home():

    return {
        "message": "Search Heist AI Backend Running"
    }


# ====================================================
# HEALTH
# ====================================================

@router.get("/health")

def health():

    return {
        "status": "healthy"
    }


# ====================================================
# FUNNEL ANALYSIS
# ====================================================

@router.post("/upload-funnel")

async def upload_funnel(
    file: UploadFile = File(...)
):

    try:

        df = pd.read_csv(file.file)

        save_latest_dataset(df)

        results = analyze_funnel(df)

        segmentation_results = analyze_segments(df)

        results[
            "segmentation_analysis"
        ] = segmentation_results

        device_results = analyze_device_performance(df)

        results[
            "device_analysis"
        ] = device_results

        save_results(results)

        return results

    except Exception as e:

        return {
            "error": True,
            "message": str(e)
        }


# ====================================================
# EXPERIMENT ANALYSIS
# ====================================================

@router.post("/upload-experiment")

async def upload_experiment(
    file: UploadFile = File(...)
):

    try:

        df = pd.read_csv(file.file)

        save_latest_dataset(df)

        results = analyze_experiment(df)

        segmentation_results = analyze_segments(df)

        results[
            "segmentation_analysis"
        ] = segmentation_results

        device_results = analyze_device_performance(df)

        results[
            "device_analysis"
        ] = device_results

        save_results(results)

        return results

    except Exception as e:

        return {
            "error": True,
            "message": str(e)
        }


# ====================================================
# ASK AI
# ====================================================

@router.post("/ask-ai")

async def ask_ai(
    request: QuestionRequest
):

    try:

        dataset_path = (
            "datasets/latest_uploaded_file.csv"
        )

        if not os.path.exists(dataset_path):

            return {
                "answer":
                "Please upload a dataset first."
            }

        df = pd.read_csv(dataset_path)

        analysis_results = analyze_experiment(df)

        segmentation_results = analyze_segments(df)

        analysis_results[
            "segmentation_analysis"
        ] = segmentation_results

        device_results = analyze_device_performance(df)

        analysis_results[
            "device_analysis"
        ] = device_results

        system_prompt = build_experiment_prompt(
            df=df,
            analysis_results=analysis_results
        )

        final_prompt = f"""
{system_prompt}

User Question:
{request.question}
"""

        response = model.generate_content(
            final_prompt
        )

        insights = [

            line.replace("*", "")
            .replace("-", "")
            .replace("•", "")
            .strip()

            for line in response.text.split("\n")

            if len(line.strip()) > 20
        ]

        if not insights:

            insights = [
                "No AI insights generated."
            ]

        return {
            "answer": insights
        }

    except Exception as e:

        return {
            "answer":
            f"Gemini Error: {str(e)}"
        }
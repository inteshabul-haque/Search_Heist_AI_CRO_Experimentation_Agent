from fastapi import APIRouter, UploadFile, File
import pandas as pd

from analytics.funnel_analysis import analyze_funnel
from analytics.experiment_analysis import analyze_experiment
from analytics.significance_test import run_significance_test

from agents.master_agent import run_master_agent

from memory.chat_memory import save_analysis

router = APIRouter()


@router.post("/upload-funnel")
async def upload_funnel(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    result = analyze_funnel(df)

    return result


@router.post("/upload-experiment")
async def upload_experiment(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    result = analyze_experiment(df)

    return result


@router.post("/significance-test")
async def significance_test(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    grouped = df.groupby("variant")

    a_data = grouped.get_group("A")
    b_data = grouped.get_group("B")

    a_total = len(a_data)
    b_total = len(b_data)

    a_converted = a_data["converted"].sum()
    b_converted = b_data["converted"].sum()

    result = run_significance_test(
        a_converted,
        a_total,
        b_converted,
        b_total
    )

    return result


@router.post("/analyze")
async def analyze_dataset(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    results = run_master_agent(df)

    # Save latest analysis in memory
    save_analysis(results)

    return results
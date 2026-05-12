from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import pandas as pd
import os

from analytics.funnel_analysis import (
    analyze_funnel
)

from analytics.experiment_analysis import (
    analyze_experiment
)

from analytics.significance_test import (
    run_significance_test
)

from analytics.segmentation_analysis import (
    analyze_segments
)

from analytics.device_analysis import (
    analyze_device_performance
)

from agents.master_agent import (
    save_results
)

from memory.chat_memory import (
    save_analysis
)

router = APIRouter()


# ============================================================
# SAVE DATASET FUNCTION
# ============================================================

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


# ============================================================
# FUNNEL ANALYSIS
# ============================================================

@router.post("/upload-funnel")

async def upload_funnel(

    file: UploadFile = File(...)

):

    try:

        # ----------------------------------------------------
        # READ DATASET
        # ----------------------------------------------------

        df = pd.read_csv(file.file)

        # ----------------------------------------------------
        # SAVE DATASET
        # ----------------------------------------------------

        save_latest_dataset(df)

        # ----------------------------------------------------
        # RUN FUNNEL ANALYSIS
        # ----------------------------------------------------

        results = analyze_funnel(df)

        # ----------------------------------------------------
        # SEGMENTATION ANALYSIS
        # ----------------------------------------------------

        segmentation_results = (
            analyze_segments(df)
        )

        results[
            "segmentation_analysis"
        ] = segmentation_results

        # ----------------------------------------------------
        # DEVICE ANALYSIS
        # ----------------------------------------------------

        device_results = (
            analyze_device_performance(df)
        )

        results[
            "device_analysis"
        ] = device_results

        # ----------------------------------------------------
        # SAVE RESULTS TO MEMORY
        # ----------------------------------------------------

        save_results(results)

        save_analysis(results)

        return results

    except Exception as e:

        return {

            "error": True,

            "message":
                str(e)
        }


# ============================================================
# EXPERIMENT ANALYSIS
# ============================================================

@router.post("/upload-experiment")

async def upload_experiment(

    file: UploadFile = File(...)

):

    try:

        # ----------------------------------------------------
        # READ DATASET
        # ----------------------------------------------------

        df = pd.read_csv(file.file)

        # ----------------------------------------------------
        # SAVE DATASET
        # ----------------------------------------------------

        save_latest_dataset(df)

        # ----------------------------------------------------
        # RUN EXPERIMENT ANALYSIS
        # ----------------------------------------------------

        results = analyze_experiment(df)

        # ----------------------------------------------------
        # SIGNIFICANCE TEST
        # ----------------------------------------------------

        if (

            "variant" in df.columns
            and "converted" in df.columns

        ):

            grouped = df.groupby("variant")

            if (

                "A" in grouped.groups
                and "B" in grouped.groups

            ):

                a_data = grouped.get_group("A")

                b_data = grouped.get_group("B")

                significance_results = (

                    run_significance_test(

                        a_converted=
                            a_data["converted"].sum(),

                        a_total=
                            len(a_data),

                        b_converted=
                            b_data["converted"].sum(),

                        b_total=
                            len(b_data)
                    )
                )

                results[
                    "significance_test"
                ] = significance_results

        # ----------------------------------------------------
        # SEGMENTATION ANALYSIS
        # ----------------------------------------------------

        segmentation_results = (
            analyze_segments(df)
        )

        results[
            "segmentation_analysis"
        ] = segmentation_results

        # ----------------------------------------------------
        # DEVICE ANALYSIS
        # ----------------------------------------------------

        device_results = (
            analyze_device_performance(df)
        )

        results[
            "device_analysis"
        ] = device_results

        # ----------------------------------------------------
        # SAVE RESULTS TO MEMORY
        # ----------------------------------------------------

        save_results(results)

        save_analysis(results)

        return results

    except Exception as e:

        return {

            "error": True,

            "message":
                str(e)
        }


# ============================================================
# SIGNIFICANCE TEST
# ============================================================

@router.post("/significance-test")

async def significance_test(

    file: UploadFile = File(...)

):

    try:

        # ----------------------------------------------------
        # READ DATASET
        # ----------------------------------------------------

        df = pd.read_csv(file.file)

        # ----------------------------------------------------
        # SAVE DATASET
        # ----------------------------------------------------

        save_latest_dataset(df)

        grouped = df.groupby("variant")

        a_data = grouped.get_group("A")

        b_data = grouped.get_group("B")

        result = run_significance_test(

            a_converted=
                a_data["converted"].sum(),

            a_total=
                len(a_data),

            b_converted=
                b_data["converted"].sum(),

            b_total=
                len(b_data)
        )

        return result

    except Exception as e:

        return {

            "error": True,

            "message":
                str(e)
        }


# ============================================================
# MASTER ANALYSIS
# ============================================================

@router.post("/analyze")

async def analyze_dataset(

    file: UploadFile = File(...)

):

    try:

        # ----------------------------------------------------
        # READ DATASET
        # ----------------------------------------------------

        df = pd.read_csv(file.file)

        # ----------------------------------------------------
        # SAVE DATASET
        # ----------------------------------------------------

        save_latest_dataset(df)

        # ----------------------------------------------------
        # RUN EXPERIMENT ANALYSIS
        # ----------------------------------------------------

        results = analyze_experiment(df)

        # ----------------------------------------------------
        # SEGMENTATION ANALYSIS
        # ----------------------------------------------------

        segmentation_results = (
            analyze_segments(df)
        )

        results[
            "segmentation_analysis"
        ] = segmentation_results

        # ----------------------------------------------------
        # DEVICE ANALYSIS
        # ----------------------------------------------------

        device_results = (
            analyze_device_performance(df)
        )

        results[
            "device_analysis"
        ] = device_results

        # ----------------------------------------------------
        # SAVE RESULTS
        # ----------------------------------------------------

        save_results(results)

        save_analysis(results)

        return results

    except Exception as e:

        return {

            "error": True,

            "message":
                str(e)
        }
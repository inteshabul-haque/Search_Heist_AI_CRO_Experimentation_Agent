import pandas as pd


def build_experiment_prompt(df=None, analysis_results=None):

    # Handle missing dataframe
    if df is None:

        return """
You are a CRO analyst.
No dataset provided.
"""

    # Handle non-dataframe inputs safely
    if not isinstance(df, pd.DataFrame):

        return f"""
You are a CRO analyst.

Data:
{df}

Generate business insights.
"""

    # Sample data
    sample_data = (
        df.head(10)
        .to_dict(orient="records")
    )

    # Columns
    columns = list(df.columns)

    # Analysis summary
    analysis_summary = ""

    if analysis_results is not None:

        analysis_summary = str(analysis_results)

    # Final prompt
    prompt = f"""
You are a senior CRO analyst.

Analyze this A/B testing dataset and generate
executive-level business insights.

Columns:
{columns}

Total Rows:
{len(df)}

Sample Data:
{sample_data}

Analysis Results:
{analysis_summary}

Provide:
- winning variant
- conversion insights
- revenue impact
- business recommendations
"""

    return prompt
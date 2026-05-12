import pandas as pd


# ============================================================
# EXPERIMENT PROMPT BUILDER
# ============================================================

def build_experiment_prompt(df):

    # --------------------------------------------------------
    # Sample Dataset
    # --------------------------------------------------------

    sample_data = (
        df.head(20)
        .to_dict(orient="records")
    )

    # --------------------------------------------------------
    # Detect Important Columns
    # --------------------------------------------------------

    columns = list(df.columns)

    # --------------------------------------------------------
    # Dynamic Prompt
    # --------------------------------------------------------

    prompt = f"""
You are a senior CRO (Conversion Rate Optimization)
and experimentation analyst.

Your task is to review the provided A/B testing dataset
and generate an executive-level business summary.

Focus on identifying:

1. Which experiment variant performed best
2. Conversion rate performance
3. Revenue impact
4. Customer engagement behavior
5. Statistical significance patterns
6. Behavioral anomalies or risks
7. Business opportunities
8. Rollout recommendations

Instructions:

- Generate 3 to 5 concise executive insights
- Use professional and business-friendly language
- Avoid technical jargon
- Focus on actionable recommendations
- Include supporting metrics where relevant
- Prioritize the most impactful findings
- Keep tone suitable for leadership stakeholders
- Insights should feel dynamic and data-driven
- Do NOT repeat generic statements
- Mention uplift, revenue, and confidence trends where possible

Dataset Metadata:

Columns:
{columns}

Total Rows:
{len(df)}

Sample Dataset:
{sample_data}

Expected Output Format:

[
    "Insight 1",
    "Insight 2",
    "Insight 3",
    "Insight 4",
    "Insight 5"
]
"""

    return prompt
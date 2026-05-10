from analytics.funnel_analysis import analyze_funnel

def funnel_agent(df):

    result = analyze_funnel(df)

    insight = (
        f"Biggest funnel drop occurs at {result['biggest_drop_stage']} "
        f"with {result['drop_count']} users dropping off."
    )

    return {
        "analysis": result,
        "insight": insight
    }
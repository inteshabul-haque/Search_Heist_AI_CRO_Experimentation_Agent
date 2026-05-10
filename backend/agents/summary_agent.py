def generate_executive_summary(results):

    summary = f"""
    Executive Summary

    Total Users: {results.get('total_users', 0)}

    Conversion Rate:
    {results.get('conversion_rate', 0)}%

    The analysis detected meaningful funnel
    and experimentation opportunities.

    Recommended Focus Areas:
    - checkout optimization
    - mobile experience
    - funnel simplification
    - experimentation scaling
    """

    return summary
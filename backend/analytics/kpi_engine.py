def calculate_kpis(df):

    total_users = len(df)

    total_conversions = df["converted"].sum()

    conversion_rate = (
        (total_conversions / total_users) * 100
        if total_users > 0 else 0
    )

    total_revenue = (
        df["revenue"].sum()
        if "revenue" in df.columns else 0
    )

    avg_order_value = (
        total_revenue / total_conversions
        if total_conversions > 0 else 0
    )

    return {
        "total_users": int(total_users),
        "total_conversions": int(total_conversions),
        "conversion_rate": round(conversion_rate, 2),
        "total_revenue": round(total_revenue, 2),
        "avg_order_value": round(avg_order_value, 2)
    }
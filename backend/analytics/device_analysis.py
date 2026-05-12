# ============================================================
# DEVICE PERFORMANCE ANALYSIS
# ============================================================

def analyze_device_performance(df):

    # --------------------------------------------------------
    # LOWERCASE COLUMNS
    # --------------------------------------------------------

    df.columns = df.columns.str.lower()

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if "device" not in df.columns:

        return {

            "error":
                "Device column not found."
        }

    device_summary = {}

    device_insights = []

    # --------------------------------------------------------
    # GROUP BY DEVICE
    # --------------------------------------------------------

    grouped = df.groupby("device")

    best_device = None

    best_cr = 0.0

    # --------------------------------------------------------
    # LOOP DEVICES
    # --------------------------------------------------------

    for device, data in grouped:

        users = len(data)

        conversions = (
            data["converted"].sum()
        )

        revenue = (

            data["revenue"].sum()

            if "revenue" in df.columns

            else 0
        )

        conversion_rate = (

            (conversions / users) * 100

            if users > 0

            else 0
        )

        avg_order_value = (

            revenue / conversions

            if conversions > 0

            else 0
        )

        # ----------------------------------------------------
        # TRACK BEST DEVICE
        # ----------------------------------------------------

        if conversion_rate > best_cr:

            best_cr = float(conversion_rate)

            best_device = str(device)

        # ----------------------------------------------------
        # SAVE DEVICE METRICS
        # ----------------------------------------------------

        device_summary[str(device)] = {

            "users":

                int(users),

            "conversions":

                int(conversions),

            "conversion_rate":

                float(round(conversion_rate, 2)),

            "revenue":

                float(round(revenue, 2)),

            "avg_order_value":

                float(round(avg_order_value, 2))
        }

    # --------------------------------------------------------
    # GENERATE INSIGHTS
    # --------------------------------------------------------

    for device, metrics in device_summary.items():

        device_insights.append(

            f"{str(device).title()} users achieved "
            f"{metrics['conversion_rate']}% "
            f"conversion rate across "
            f"{metrics['users']} users, generating "
            f"${metrics['revenue']} revenue with "
            f"${metrics['avg_order_value']} AOV."
        )

    # --------------------------------------------------------
    # BEST DEVICE INSIGHT
    # --------------------------------------------------------

    if best_device:

        device_insights.insert(

            0,

            f"{best_device.title()} users delivered "
            f"the strongest conversion performance "
            f"at {float(round(best_cr, 2))}% conversion rate."
        )

    # --------------------------------------------------------
    # RETURN
    # --------------------------------------------------------

    return {

        "best_device":

            str(best_device)

            if best_device

            else None,

        "device_insights":

            list(device_insights),

        "device_summary":

            dict(device_summary)
    }
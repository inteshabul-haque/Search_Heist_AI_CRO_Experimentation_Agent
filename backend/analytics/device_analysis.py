def analyze_device_performance(df):

    if "device" not in df.columns:

        return {
            "error": "Device column not found."
        }

    device_summary = {}

    grouped = df.groupby("device")

    for device, data in grouped:

        users = len(data)

        conversions = data["converted"].sum()

        conversion_rate = (
            (conversions / users) * 100
            if users > 0 else 0
        )

        device_summary[device] = {
            "users": int(users),
            "conversions": int(conversions),
            "conversion_rate": round(conversion_rate, 2)
        }

    return device_summary
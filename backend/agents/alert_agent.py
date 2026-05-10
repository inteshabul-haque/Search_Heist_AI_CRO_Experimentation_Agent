def generate_alerts(results):

    alerts = []

    # KPI Alerts
    if "kpis" in results:

        kpis = results["kpis"]

        conversion_rate = kpis.get(
            "conversion_rate",
            0
        )

        if conversion_rate < 2:

            alerts.append({
                "severity": "high",
                "message": "Critical low conversion rate detected."
            })

        elif conversion_rate < 5:

            alerts.append({
                "severity": "medium",
                "message": "Moderate conversion performance detected."
            })

    # Device Alerts
    if "device_analysis" in results:

        devices = results["device_analysis"]

        for device, values in devices.items():

            cr = values.get(
                "conversion_rate",
                0
            )

            if cr < 2:

                alerts.append({
                    "severity": "high",
                    "message": (
                        f"Very weak conversion performance "
                        f"on {device}."
                    )
                })

    # Funnel Alerts
    if "funnel_analysis" in results:

        funnel = results["funnel_analysis"]

        drop_count = funnel.get(
            "drop_count",
            0
        )

        if drop_count > 100:

            alerts.append({
                "severity": "high",
                "message": (
                    "Severe funnel leakage detected."
                )
            })

    if len(alerts) == 0:

        alerts.append({
            "severity": "low",
            "message": "No major risks detected."
        })

    return alerts
def generate_chart_data(results):

    charts = {}

    # Funnel chart
    if "funnel_analysis" in results:

        funnel = results["funnel_analysis"]["funnel"]

        charts["funnel_chart"] = {
            "labels": list(funnel.keys()),
            "values": list(funnel.values())
        }

    # Experiment comparison chart
    if "experiment_analysis" in results:

        experiment_data = results["experiment_analysis"]

        variants = []
        conversion_rates = []

        for variant, values in experiment_data.items():

            variants.append(variant)

            conversion_rates.append(
                values["conversion_rate"]
            )

        charts["experiment_chart"] = {
            "labels": variants,
            "values": conversion_rates
        }

    # Device performance chart
    if "device_analysis" in results:

        device_data = results["device_analysis"]

        devices = []
        device_cr = []

        for device, values in device_data.items():

            devices.append(device)

            device_cr.append(
                values["conversion_rate"]
            )

        charts["device_chart"] = {
            "labels": devices,
            "values": device_cr
        }

    return charts
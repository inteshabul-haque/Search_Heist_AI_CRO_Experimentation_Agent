def generate_tactical_alerts(results):

    alerts = []

    conversion_rate = results.get(
        "conversion_rate",
        0
    )

    uplift = results.get(
        "uplift",
        0
    )

    p_value = results.get(
        "p_value",
        1
    )

    # -----------------------------------
    # LOW CONVERSION
    # -----------------------------------

    if conversion_rate < 3:

        alerts.append({

            "severity": "critical",

            "message":
            "Conversion rate is critically low."
        })

    elif conversion_rate < 8:

        alerts.append({

            "severity": "medium",

            "message":
            "Conversion rate below benchmark."
        })

    # -----------------------------------
    # UPLIFT
    # -----------------------------------

    if uplift > 15:

        alerts.append({

            "severity": "positive",

            "message":
            "Experiment shows strong uplift."
        })

    elif uplift < 0:

        alerts.append({

            "severity": "critical",

            "message":
            "Variant performance declined."
        })

    # -----------------------------------
    # SIGNIFICANCE
    # -----------------------------------

    if p_value > 0.05:

        alerts.append({

            "severity": "medium",

            "message":
            "Experiment lacks statistical significance."
        })

    return alerts
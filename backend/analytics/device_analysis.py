def analyze_device_segments(df):

    # -----------------------------------
    # POSSIBLE DEVICE COLUMNS
    # -----------------------------------

    possible_columns = [

        "device",
        "device_type",
        "platform"
    ]

    device_column = None

    for col in possible_columns:

        if col in df.columns:

            device_column = col

            break

    # -----------------------------------
    # NO DEVICE DATA
    # -----------------------------------

    if not device_column:

        return None

    # -----------------------------------
    # CALCULATE DISTRIBUTION
    # -----------------------------------

    total = len(df)

    distribution = (

        df[device_column]

        .value_counts(normalize=True)

        * 100
    )

    segments = []

    for device, pct in distribution.items():

        segments.append({

            "label": str(device),

            "value":
            f"{round(float(pct), 1)}%"
        })

    return segments
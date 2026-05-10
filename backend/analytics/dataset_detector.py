def detect_dataset_type(df):

    columns = [col.lower() for col in df.columns]

    if "variant" in columns:
        return "experiment"

    if "visit" in columns:
        return "funnel"

    return "unknown"
def profile_dataset(df):

    profile = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": list(df.columns),
        "missing_values": {},
        "data_types": {},
        "numeric_columns": [],
        "categorical_columns": []
    }

    for column in df.columns:

        # Missing values
        profile["missing_values"][column] = int(
            df[column].isnull().sum()
        )

        # Data type
        profile["data_types"][column] = str(df[column].dtype)

        # Numeric vs categorical
        if df[column].dtype in ["int64", "float64"]:

            profile["numeric_columns"].append(column)

        else:

            profile["categorical_columns"].append(column)

    return profile
import numpy as np


def make_json_safe(data):

    # -----------------------------------
    # DICTIONARY
    # -----------------------------------

    if isinstance(data, dict):

        return {

            str(key): make_json_safe(value)

            for key, value in data.items()
        }

    # -----------------------------------
    # LIST
    # -----------------------------------

    elif isinstance(data, list):

        return [
            make_json_safe(item)
            for item in data
        ]

    # -----------------------------------
    # NUMPY INTEGER
    # -----------------------------------

    elif isinstance(data, np.integer):

        return int(data)

    # -----------------------------------
    # NUMPY FLOAT
    # -----------------------------------

    elif isinstance(data, np.floating):

        return float(data)

    # -----------------------------------
    # NUMPY ARRAY
    # -----------------------------------

    elif isinstance(data, np.ndarray):

        return data.tolist()

    # -----------------------------------
    # NUMPY BOOLEAN
    # -----------------------------------

    elif isinstance(data, np.bool_):

        return bool(data)

    # -----------------------------------
    # TUPLE
    # -----------------------------------

    elif isinstance(data, tuple):

        return tuple(
            make_json_safe(item)
            for item in data
        )

    # -----------------------------------
    # EVERYTHING ELSE
    # -----------------------------------

    return data
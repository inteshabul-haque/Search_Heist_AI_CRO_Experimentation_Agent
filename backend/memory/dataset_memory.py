latest_dataset = None


def save_dataset(df):

    global latest_dataset

    latest_dataset = df


def get_dataset():

    return latest_dataset
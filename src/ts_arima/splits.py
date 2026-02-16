import pandas as pd
from .config import TRAIN_RATIO


def time_series_split(series: pd.Series, train_ratio: float = TRAIN_RATIO):
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    n = len(series)
    split_index = int(n * train_ratio)

    train = series.iloc[:split_index]
    test = series.iloc[split_index:]

    return train, test

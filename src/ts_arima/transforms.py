import numpy as np
import pandas as pd

def compute_log_returns(prices: pd.Series) -> pd.Series:
    """
    Compute log returns from a price series.
    log_return[t] = log(price[t]) - log(price[t-1])
    """
    log_returns = np.log(prices).diff()
    return log_returns.dropna()


def difference(series: pd.Series, order: int = 1) -> pd.Series:
    """
    Apply differencing of arbitrary order.
    Useful for making a series stationary.
    """
    diffed = series.copy()
    for _ in range(order):
        diffed = diffed.diff()

    return diffed.dropna()

def invert_difference(last_observation: float, diff_value: float) -> float:
    """
    Reconstruct the original value from a differenced forecast.
    For ARIMA models where d > 0.
    """
    return last_observation + diff_value

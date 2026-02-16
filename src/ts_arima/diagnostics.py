import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
from .config import FIGURES_DIR
import os


def adf_test(series: pd.Series) -> dict:
    """
    Run Augmented Dickey-Fuller test on a time series.
    Returns a dictionary with key statistics.
    """
    result = adfuller(series.dropna())

    return {
        "ADF Statistic": result[0],
        "p-value": result[1],
        "Lags Used": result[2],
        "Observations": result[3],
        "Critical Values": result[4]
    }

def plot_acf_pacf(series: pd.Series, lags: int = 40, save_name: str = None):
    """
    Plot ACF and PACF side-by-side.
    Optionally save the figure to the reports/figures directory.
    """
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    plot_acf(series.dropna(), lags=lags, ax=ax[0])
    ax[0].set_title("ACF")

    plot_pacf(series.dropna(), lags=lags, ax=ax[1])
    ax[1].set_title("PACF")

    plt.tight_layout()

    if save_name:
        path = os.path.join(FIGURES_DIR, save_name)
        fig.savefig(path)
        print(f"Saved ACF/PACF plot to: {path}")

    return fig


def plot_series(series: pd.Series, title: str, save_name: str = None):
    """
    Generic line plot for any time series (prices, returns, etc.)
    """
    plt.figure(figsize=(10, 4))
    plt.plot(series.index, series.values)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.tight_layout()

    if save_name:
        path = os.path.join(FIGURES_DIR, save_name)
        plt.savefig(path)
        print(f"Saved plot to: {path}")

    return plt
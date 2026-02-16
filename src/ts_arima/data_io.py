import pandas as pd
from .config import RAW_DATA_PATH, PROCESSED_DATA_PATH

def load_raw_prices(path: str = RAW_DATA_PATH) -> pd.Series:
    """
    Load raw DAX price data from CSV.
    Expects a 'Close' column and a 'Date' index.
    """
    df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")

    if "Close" not in df.columns:
        raise ValueError("Expected column 'Close' in raw price file.")

    return df["Close"]


def load_returns(path: str = PROCESSED_DATA_PATH) -> pd.Series:
    """
    Load processed log-return series from CSV.
    Expects a 'LogReturn' column and a 'Date' index.
    """
    df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")

    if "LogReturn" not in df.columns:
        raise ValueError("Expected column 'LogReturn' in processed returns file.")

    return df["LogReturn"]


def save_series(series: pd.Series, path: str):
    """
    Save a pandas Series to CSV with its index.
    """
    series.to_csv(path, header=True)

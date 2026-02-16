import pandas as pd
import numpy as np

RAW_PATH = r"E:\Personal\GitHub\Python Code Repo\time-series-arima-dax\data\raw\dax_prices.csv"
PROCESSED_PATH = r"E:\Personal\GitHub\Python Code Repo\time-series-arima-dax\data\processed\dax_returns.csv"

def create_log_returns():
    print("Loading raw DAX prices...")
    df = pd.read_csv(RAW_PATH, parse_dates=["Date"], index_col="Date")

    if "Close" not in df.columns:
        raise ValueError("ERROR: 'Close' column not found in dax_prices.csv")

    # Compute log returns
    df["LogReturn"] = np.log(df["Close"]).diff()

    # Clean missing values (first row will be NaN)
    df = df.dropna(subset=["LogReturn"])

    # Save only the returns column
    returns = df[["LogReturn"]]
    returns.to_csv(PROCESSED_PATH)

    print(f"Log returns saved to: {PROCESSED_PATH}")

if __name__ == "__main__":
    create_log_returns()
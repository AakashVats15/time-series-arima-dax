import os
import sys
import traceback

import pandas as pd

from ts_arima.config import (
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH,
    FIGURES_DIR,
    ARIMA_ORDER,
    FORECAST_HORIZON,
)
from ts_arima.data_io import load_raw_prices, load_returns, save_series
from ts_arima.transforms import compute_log_returns
from ts_arima.diagnostics import adf_test, plot_acf_pacf, plot_series
from ts_arima.splits import time_series_split
from ts_arima.models import ARIMAModel


def ensure_directories():
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    os.makedirs(FIGURES_DIR, exist_ok=True)


def prepare_returns() -> pd.Series:
    """
    Load raw prices, compute log returns, save processed returns, and return the series.
    """
    if not os.path.exists(RAW_DATA_PATH):
        raise FileNotFoundError(
            f"Raw prices file not found at:\n{RAW_DATA_PATH}\n"
            "Make sure dax_prices.csv is downloaded and placed there."
        )

    print(f"Loading raw prices from: {RAW_DATA_PATH}")
    prices = load_raw_prices()

    print(f"Loaded {len(prices)} price points. First 5:\n{prices.head()}\n")

    print("Computing log returns...")
    returns = compute_log_returns(prices)
    print(f"Computed {len(returns)} log-return points. First 5:\n{returns.head()}\n")

    print(f"Saving log returns to: {PROCESSED_DATA_PATH}")
    save_series(returns.rename("LogReturn"), PROCESSED_DATA_PATH)

    return returns


def run_diagnostics(prices: pd.Series, returns: pd.Series):
    """
    Run basic diagnostics: plots and ADF test.
    """
    print("Running ADF test on log returns...")
    adf_results = adf_test(returns)
    print("ADF Test Results:")
    for k, v in adf_results.items():
        print(f"  {k}: {v}")
    print()

    print("Creating diagnostic plots...")
    plot_series(prices, "DAX Close Prices", save_name="dax_prices.png")
    plot_series(returns, "DAX Log Returns", save_name="dax_log_returns.png")
    plot_acf_pacf(returns, lags=40, save_name="dax_returns_acf_pacf.png")
    print(f"Plots saved in: {FIGURES_DIR}\n")


def train_and_forecast(returns: pd.Series):
    """
    Split returns into train/test, fit ARIMA, and forecast.
    """
    print("Splitting data into train and test sets...")
    train, test = time_series_split(returns)
    print(f"Train length: {len(train)}, Test length: {len(test)}\n")

    print(f"Fitting ARIMA model with order={ARIMA_ORDER}...")
    model = ARIMAModel(order=ARIMA_ORDER)
    model.fit(train)
    print("Model fitted.\n")

    steps = len(test) if FORECAST_HORIZON == 1 else FORECAST_HORIZON
    print(f"Forecasting {steps} step(s)...")
    forecast = model.forecast(steps=steps)

    # Align forecast with test index if same length
    if len(forecast) == len(test):
        forecast.index = test.index

    print("Model summary:")
    print(model.summary())
    print()

    print("Forecast vs actual (last 10 rows):")
    df_compare = pd.DataFrame(
        {
            "Actual": test[-10:],
            "Forecast": forecast[-10:] if len(forecast) >= 10 else forecast,
        }
    )
    print(df_compare)
    print()

    # Simple error metric if lengths match
    if len(forecast) == len(test):
        mse = ((forecast - test) ** 2).mean()
        print(f"Mean Squared Error on test set: {mse:.6f}\n")


def main():
    try:
        ensure_directories()

        # Step 1: Prepare returns (from raw prices)
        returns = prepare_returns()

        # Step 2: Load prices again for plotting (already on disk)
        prices = load_raw_prices()

        # Step 3: Diagnostics
        run_diagnostics(prices, returns)

        # Step 4: Train ARIMA and forecast
        train_and_forecast(returns)

        print("Pipeline completed successfully.")

    except Exception as e:
        print("ERROR: An exception occurred while running the pipeline.\n")
        print(e)
        print()
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
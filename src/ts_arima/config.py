import os
# Base project directory
BASE_DIR = r"E:\Personal\GitHub\Python Code Repo\time-series-arima-dax"

# Data paths
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "dax_prices.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "dax_returns.csv")

# Reports path
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
FIGURES_DIR = os.path.join(REPORTS_DIR, "figures")

INSTRUMENT = "DAX"
FORECAST_HORIZON = 1  # 1-day ahead forecast

# (p, d, q) — can be tuned as per requirements
ARIMA_ORDER = (1, 0, 1)

# Train/test split ratio
TRAIN_RATIO = 0.8
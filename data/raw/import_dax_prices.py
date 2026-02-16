import pandas as pd

INPUT_PATH = r"E:\Personal\GitHub\Python Code Repo\time-series-arima-dax\data\raw\dax_prices.csv"
OUTPUT_PATH = INPUT_PATH  # overwrite same file

df = pd.read_csv(INPUT_PATH)

# Ensure Date is datetime
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

# Keep only Close column
df = df[["Close"]]

# Clean missing values
df = df.dropna()
df = df.ffill()
df = df.bfill()

df.to_csv(OUTPUT_PATH)
print("Cleaned DAX data saved.")

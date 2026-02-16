# Time-Series ARIMA trained on DAX

This repository implements a complete Python-based ARIMA workflow using the DAX index as the single chosen dataset. The project focuses on data processing, diagnostics, model training, and forecasting using a clean, modular code structure.

All theoretical explanations (stationarity, ACF/PACF, AR/MA/ARIMA, returns vs prices) are available in the Wiki.

---

## Project Structure

```
time-series-arima-dax/
├─ README.md
├─ requirements.txt
├─ data/
│  ├─ raw/
│  │  └─ dax_prices.csv
│  └─ processed/
│     └─ dax_returns.csv
├─ src/
│  └─ ts_arima/
│     ├─ __init__.py
│     ├─ config.py
│     ├─ data_io.py
│     ├─ transforms.py
│     ├─ diagnostics.py
│     ├─ models.py
│     ├─ splits.py
│     └─ main.py
└─ reports/
   ├─ figures/
   └─ summary.md
```

---

## Folder Overview

### `data/`
Contains raw DAX price data and processed log-return series.

### `src/ts_arima/`
Core Python package implementing the workflow:
- `config.py` — instrument selection and paths  
- `data_io.py` — load/save time-series data  
- `transforms.py` — log-returns and differencing  
- `diagnostics.py` — ADF test and ACF/PACF plotting  
- `splits.py` — time-based train/test split  
- `models.py` — ARIMA model wrapper  
- `main.py` — end-to-end execution script  

### `reports/`
Stores generated figures and a summary of results.

---

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Place your DAX price file in:
   ```
   data/raw/dax_prices.csv
   ```

3. Run the full pipeline:
   ```bash
   python src/ts_arima/main.py
   ```

This will:
- Load prices  
- Compute log-returns  
- Run diagnostics  
- Generate ACF/PACF plots  
- Perform a time-based train/test split  
- Fit an ARIMA model  
- Produce a 1-day forecast  
- Save outputs to `reports/`  

---

## Theory

All theoretical explanations are available in the Wiki.

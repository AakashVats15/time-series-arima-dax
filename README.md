# 📈 Time-Series ARIMA on DAX

This repository implements a complete **Python-based ARIMA workflow** using the **DAX index** as the single dataset. It includes data processing, diagnostics, model training, and forecasting — all organized into clean, modular Python scripts.

📚 All theoretical explanations are available in the **Wiki**.

---

## 📁 Project Structure

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

## 📦 Folder Overview

### `data/`
📊 Raw DAX prices and processed log-return data.

### `src/ts_arima/`
🧩 Core Python package:
- `config.py` — settings and paths  
- `data_io.py` — load/save data  
- `transforms.py` — log-returns, differencing  
- `diagnostics.py` — ADF, ACF/PACF  
- `splits.py` — time-based train/test split  
- `models.py` — ARIMA wrapper  
- `main.py` — full pipeline runner  

### `reports/`
🖼️ Generated figures and summary outputs.

---

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Add your DAX price file:
   ```
   data/raw/dax_prices.csv
   ```

3. Run the pipeline:
   ```bash
   python src/ts_arima/main.py
   ```

This will:
- Load prices  
- Compute log-returns  
- Run diagnostics  
- Generate ACF/PACF plots  
- Split train/test  
- Fit ARIMA  
- Produce a 1‑day forecast  
- Save results to `reports/`  

---

## 📘 Theory

All theoretical explanations are available in the **Wiki**.
```
import sys
import os

# Force-add src to sys.path
ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)

from ts_arima.main import main

if __name__ == "__main__":
    main()
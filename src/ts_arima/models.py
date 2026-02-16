import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from .config import ARIMA_ORDER, FORECAST_HORIZON


class ARIMAModel:

    def __init__(self, order: tuple = ARIMA_ORDER):
        self.order = order
        self.model_fit = None

    def fit(self, train_series: pd.Series):
        """
        Fit an ARIMA model to the training data.
        """
        model = ARIMA(train_series, order=self.order)
        self.model_fit = model.fit()
        return self.model_fit

    def forecast(self, steps: int = FORECAST_HORIZON) -> pd.Series:
        """
        Forecast future values using the fitted ARIMA model.
        """
        if self.model_fit is None:
            raise RuntimeError("Model must be fitted before forecasting.")

        forecast = self.model_fit.forecast(steps=steps)
        return forecast

    def summary(self) -> str:
        """
        Return the model summary as text.
        """
        if self.model_fit is None:
            raise RuntimeError("Model must be fitted before requesting summary.")

        return self.model_fit.summary().as_text()
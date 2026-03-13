import numpy as np
import pandas as pd

class TimeSeriesEngine:
    def __init__(self, data):
        self.data = data # Specific product dataframe

    def forecast_prices(self, horizon_months=6):
        """Linear Regression Projection using Numpy Polyfit."""
        y = self.data['price'].values
        x = np.arange(len(y))
        
        # Fit 1st degree polynomial
        coefficients = np.polyfit(x, y, 1)
        polynomial = np.poly1d(coefficients)
        
        # Predict future steps
        future_x = np.arange(len(y), len(y) + horizon_months)
        return polynomial(future_x)

    def get_summary_stats(self):
        return {
            "min": self.data['price'].min(),
            "max": self.data['price'].max(),
            "avg": self.data['price'].mean(),
            "current": self.data['price'].iloc[-1]
        }


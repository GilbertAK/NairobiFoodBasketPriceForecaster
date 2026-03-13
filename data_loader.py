import pandas as pd
import numpy as np
from datetime import datetime, timedelta
try:
    from .config import COMMODITIES, BASE_PRICES
except ImportError:
    from config import COMMODITIES, BASE_PRICES

class DataLoader:
    def generate_simulated_data(self, months=36):
        """Generates 3 years of price history based on Nairobi trends."""
        data = []
        end_date = datetime.now()
        start_date = end_date - timedelta(days=months * 30)
        # date_range = pd.date_range(start=start_date, end=end_date, freq='ME')
        date_range = pd.date_range(start=start_date, end=end_date, freq='M')
        
        for product in COMMODITIES:
            base = BASE_PRICES[product]
            for i, date in enumerate(date_range):
                seasonality = 8 * np.sin(2 * np.pi * i / 12)
                inflation = (base * 0.007 * i) # 0.7% monthly average
                noise = np.random.normal(0, 1.5)
                price = max(10, base + seasonality + inflation + noise)
                data.append({"date": date, "product": product, "price": round(price, 2)})
        return pd.DataFrame(data)


import matplotlib.pyplot as plt
import pandas as pd

class Visualizer:
    def __init__(self, color="#ff4b4b"):
        plt.style.use('dark_background')
        self.color = color

    def show_terminal_plot(self, history_dates, history_prices, forecast_prices, product_name):
        """Generates a Matplotlib window for local testing."""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Historical Data
        ax.plot(history_dates, history_prices, label="Historical", color=self.color, marker='o', markersize=4)
        
        # Forecast Data
        last_date = history_dates.iloc[-1]
        forecast_dates = [last_date + pd.DateOffset(months=i+1) for i in range(len(forecast_prices))]
        ax.plot(forecast_dates, forecast_prices, '--', label="6-Month Forecast", color="#44ff44", linewidth=2)
        
        ax.set_title(f"Nairobi Market Analysis: {product_name}", fontsize=14)
        ax.set_ylabel("Price (KSh)")
        ax.legend()
        ax.grid(alpha=0.1)
        
        print(f"\n[Visualizer] Plot generated for {product_name}. Close window to continue.")
        plt.show()



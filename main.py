from data_loader import DataLoader
from preprocessor import DataPreprocessor
from ts_engine import TimeSeriesEngine
from visualizer import Visualizer
import utils
from config import COMMODITIES

def main():
    print("="*50)
    print(" NAIROBI FOOD BASKET - TERMINAL ANALYZER ")
    print("="*50)

    # 1. Load & Clean
    loader = DataLoader()
    raw_df = loader.generate_simulated_data()
    df = DataPreprocessor.clean_data(raw_df)

    # 2. Select Product (Testing for 'Maize Flour (2kg)')
    target_product = COMMODITIES[0]
    product_df = DataPreprocessor.filter_by_product(df, target_product)

    # 3. Analyze
    engine = TimeSeriesEngine(product_df)
    stats = engine.get_summary_stats()
    forecast = engine.forecast_prices(horizon_months=6)

    # 4. Console Output
    print(f"\nPRODUCT: {target_product}")
    print(f"Current Price : {utils.format_currency(stats['current'])}")
    print(f"Historical Min: {utils.format_currency(stats['min'])}")
    print(f"Historical Max: {utils.format_currency(stats['max'])}")
    
    change = utils.calculate_percentage_change(stats['avg'], forecast[-1])
    print(f"Projected Change (6mo): {change:.2f}% {utils.get_growth_label(change)}")

    # 5. Graphical Output
    viz = Visualizer(color="#ff4b4b")
    viz.show_terminal_plot(product_df['date'], product_df['price'], forecast, target_product)

if __name__ == "__main__":
    main()

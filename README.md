# 🌽 Nairobi Food Basket Price Forecaster

## 📌 Project Overview
An advanced Time Series analysis and forecasting engine designed to predict market trends for essential food commodities in Nairobi, Kenya. This project utilizes mathematical projections to provide market intelligence for stakeholders in the regional agricultural sector.

## 🚀 Technical Highlights
* **Modular Architecture:** Logic is decoupled into 7 specialized Python modules.
* **Mathematical Forecasting:** Uses Numpy-based trend analysis (Linear/Polynomial) for future price projections.
* **Localized Context:** Data modeling based on Kenya National Bureau of Statistics (KNBS) inflation trends.

## 📂 Repository Structure
- `main.py`: Application entry point.
- `data_loader.py`: Ingestion logic.
- `preprocessor.py`: Data cleaning and feature engineering.
- `ts_engine.py`: Core Time Series mathematical logic.
- `visualizer.py`: Matplotlib plotting engine.
- `config.py`: Global constants and product definitions.
- `utils.py`: Currency and percentage helper functions.

## 🛠️ Installation
1. `pip install -r requirements.txt`
2. `streamlit run main.py`

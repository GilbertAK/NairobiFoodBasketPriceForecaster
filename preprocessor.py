import pandas as pd


class DataPreprocessor:
    @staticmethod
    def clean_data(df):
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by=['product', 'date'])
        # Remplacez fillna(method='ffill') par ffill() pour la compatibilité
        return df.ffill() 

    @staticmethod
    def filter_by_product(df, product_name):
        return df[df['product'] == product_name].reset_index(drop=True)


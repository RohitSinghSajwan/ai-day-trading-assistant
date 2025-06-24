import pandas as pd
def load_tickers():
    return pd.read_csv("global_t212_stocks.csv")

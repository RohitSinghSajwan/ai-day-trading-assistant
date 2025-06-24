import streamlit as st
from global_stock_loader import load_tickers
from ranker import top_stocks
import yfinance as yf

st.set_page_config(page_title="AI Pro Trader", layout="wide")
st.markdown("# 📈 AI Trading212 Assistant — Top Daily Buys")

df = load_tickers()
tickers = df["Ticker"].tolist()
buys = top_stocks(tickers)

for ticker, score, pat in buys:
    info = yf.Ticker(ticker).info
    st.markdown(f"## {ticker} — £{info['regularMarketPrice']:.2f}")
    st.write(f"Sentiment Score: {score:.2f}")
    st.write(f"Pattern: {pat or '–'}")
    st.write(f"[View chart on TradingView](https://www.tradingview.com/symbols/{ticker})")

import yfinance as yf
import ta

def detect_pattern(ticker):
    df = yf.download(ticker, period="5d", interval="30m")
    if len(df) < 20: return ""
    rsi = ta.momentum.RSIIndicator(df["Close"]).rsi().iloc[-1]
    sma = ta.trend.SMAIndicator(df["Close"], window=20).sma_indicator().iloc[-1]
    if df["Close"].iloc[-1] > sma and rsi < 70:
        return "Bullish Setup"
    return ""

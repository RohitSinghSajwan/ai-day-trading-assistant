from news_sentiment import score_news
from pattern_detector import detect_pattern

def score_stock(ticker):
    sentiment = score_news(ticker)
    pattern = detect_pattern(ticker)
    base = sentiment + (0.5 if pattern else 0)
    return base, pattern

def top_stocks(tickers, top_n=5):
    scored = [(t, *score_stock(t)) for t in tickers]
    scored = [(t,s,p) for t,s,p in scored if s > 0.3]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_n]

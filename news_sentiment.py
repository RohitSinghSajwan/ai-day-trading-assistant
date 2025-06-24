import requests
import pandas as pd
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from nltk.data import find

try:
    find('sentiment/vader_lexicon.zip')
except:
    nltk.download('vader_lexicon')

def fetch_headlines(ticker):
    params = {"q": ticker, "tbm": "nws", "tbs": "qdr:d"}
    res = requests.get("https://www.google.com/search", params=params, headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    return [elt.get_text() for elt in soup.select(".BNeawe.vvjwJb")][:5]

def score_news(ticker):
    headlines = fetch_headlines(ticker)
    scores = [sid.polarity_scores(h)["compound"] for h in headlines]
    return max(scores) if scores else 0

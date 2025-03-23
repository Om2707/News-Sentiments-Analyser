import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """Perform sentiment analysis on text"""
    score = sia.polarity_scores(text)
    if score["compound"] > 0.05:
        return "Positive"
    elif score["compound"] < -0.05:
        return "Negative"
    else:
        return "Neutral"

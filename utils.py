import requests
from sentiment import analyze_sentiment

API_KEY = " " # Replace with your NewsAPI Key
NEWS_API_URL = "https://newsapi.org/v2/everything"

def fetch_news(company):
    """Fetch news articles specifically about the given company"""
    params = {
        "q": company, 
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }

    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    if data.get("status") != "ok":
        return {"error": "Failed to fetch news"}

    articles = []
    for article in data.get("articles", [])[:20]:  
        title = article.get("title", "No Title")
        summary = article.get("description", "Summary not available")
        link = article.get("url", "#")

        if company.lower() in title.lower() or company.lower() in summary[:100].lower():
            sentiment = analyze_sentiment(summary)
            articles.append({"title": title, "summary": summary, "link": link, "sentiment": sentiment})

        if len(articles) >= 10:
            break

    if not articles:
        return {"error": f"No relevant articles found for {company}"}

    return articles

def comparative_analysis(articles):
    """Analyze sentiment distribution across articles"""
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for article in articles:
        sentiment_counts[article["sentiment"]] += 1

    return sentiment_counts

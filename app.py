import gradio as gr
from utils import fetch_news, comparative_analysis
from tts import text_to_speech

def analyze_company_news(company):
    """Fetch news, analyze sentiment, and return TTS"""
    articles = fetch_news(company)
    if "error" in articles:
        return "Error fetching news. Try again."

    analysis = comparative_analysis(articles)
    
    summary_text = f"Positive: {analysis['Positive']}, Negative: {analysis['Negative']}, Neutral: {analysis['Neutral']}"
    audio_file = text_to_speech(summary_text)

    return articles, analysis, audio_file

iface = gr.Interface(
    fn=analyze_company_news,
    inputs="text",
    outputs=["json", "json", "file"],
    title="Company News Sentiment Analyzer",
    description="Enter a company name to get news, sentiment analysis, and a Hindi TTS report."
)

iface.launch()

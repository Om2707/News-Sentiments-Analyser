from flask import Flask, request, jsonify
from utils import fetch_news, comparative_analysis
from tts import text_to_speech

app = Flask(__name__)

@app.route("/news", methods=["GET"])
def get_news():
    """Fetch news and perform sentiment analysis"""
    company = request.args.get("company")
    if not company:
        return jsonify({"error": "Please provide a company name"}), 400

    articles = fetch_news(company)
    if "error" in articles:
        return jsonify(articles), 500

    analysis = comparative_analysis(articles)
    
    summary_text = f"Positive: {analysis['Positive']}, Negative: {analysis['Negative']}, Neutral: {analysis['Neutral']}"
    audio_file = text_to_speech(summary_text)

    return jsonify({
        "company": company,
        "articles": articles,
        "analysis": analysis,
        "audio": audio_file
    })

if __name__ == "__main__":
    app.run(debug=True)

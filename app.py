import dns.resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4']

from flask import Flask, render_template, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.outbreak_db

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/hotspots")
def get_hotspots():
    try:
        hotspots = list(db.hotspots.find({}, {"_id": 0}))
        return jsonify(hotspots)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/news")
def get_news():
    try:
        news = list(db.news_articles.find(
            {}, {"_id": 0, "title": 1, "description": 1,
                 "url": 1, "source": 1, "published_at": 1, "keyword": 1}
        ).sort("published_at", -1).limit(20))
        return jsonify(news)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/stats")
def get_stats():
    try:
        total_articles = db.news_articles.count_documents({})
        total_hotspots = db.hotspots.count_documents({})
        high_risk = db.hotspots.count_documents({"risk_level": "HIGH"})
        medium_risk = db.hotspots.count_documents({"risk_level": "MEDIUM"})
        low_risk = db.hotspots.count_documents({"risk_level": "LOW"})
        return jsonify({
            "total_articles": total_articles,
            "total_hotspots": total_hotspots,
            "high_risk": high_risk,
            "medium_risk": medium_risk,
            "low_risk": low_risk
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
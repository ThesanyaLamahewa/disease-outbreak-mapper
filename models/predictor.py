import dns.resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime, timezone
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client.outbreak_db

COUNTRIES = [
    "USA", "United States", "UK", "United Kingdom", "India", "China",
    "Brazil", "France", "Germany", "Italy", "Spain", "Japan", "Australia",
    "Canada", "Mexico", "Russia", "South Africa", "Nigeria", "Pakistan",
    "Bangladesh", "Indonesia", "Sri Lanka", "Thailand", "Philippines"
]

RISK_WEIGHTS = {
    "outbreak": 10, "epidemic": 15, "pandemic": 20,
    "deaths": 10, "fatalities": 10, "spreading": 8,
    "surge": 7, "spike": 7, "emergency": 9,
    "quarantine": 8, "lockdown": 8, "infection": 6,
    "cases": 4, "flu": 3, "virus": 3, "disease": 3,
    "cholera": 12, "dengue": 10, "measles": 8, "covid": 8,
}

def calculate_risk_score(text):
    if not text:
        return 0
    text_lower = text.lower()
    score = 0
    for keyword, weight in RISK_WEIGHTS.items():
        count = text_lower.count(keyword)
        score += count * weight
    return min(score, 100)

def extract_countries(text):
    if not text:
        return []
    found = []
    for country in COUNTRIES:
        if country.lower() in text.lower():
            found.append(country)
    return found

def run_predictions():
    print("🤖 Running AI predictions...")
    articles = list(db.news_articles.find())
    print(f"📰 Analysing {len(articles)} articles...")

    country_scores = {}
    country_article_count = {}

    for article in articles:
        text = " ".join(filter(None, [
            article.get("title", ""),
            article.get("description", ""),
            article.get("content", "")
        ]))

        score = calculate_risk_score(text)
        countries = extract_countries(text)

        if not countries:
            countries = ["Unknown"]

        for country in countries:
            if country not in country_scores:
                country_scores[country] = 0
                country_article_count[country] = 0
            country_scores[country] += score
            country_article_count[country] += 1

    db.hotspots.delete_many({})
    hotspots = []

    for country, total_score in country_scores.items():
        count = country_article_count[country]
        avg_score = round(total_score / count, 2)

        if avg_score >= 70:
            risk_level = "HIGH"
        elif avg_score >= 40:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        hotspot = {
            "country": country,
            "risk_score": avg_score,
            "risk_level": risk_level,
            "article_count": count,
            "updated_at": datetime.now(timezone.utc)
        }
        db.hotspots.insert_one(hotspot)
        hotspots.append(hotspot)

    hotspots.sort(key=lambda x: x["risk_score"], reverse=True)

    print("\n🌍 TOP HOTSPOTS:")
    print("-" * 50)
    for h in hotspots[:10]:
        print(f"{h['risk_level']:6} | Score: {h['risk_score']:6} | {h['country']}")

    print(f"\n✅ Saved {len(hotspots)} hotspots to MongoDB!")
    return hotspots

if __name__ == "__main__":
    run_predictions()
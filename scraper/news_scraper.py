import dns.resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

import requests
from datetime import datetime, timezone
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client.outbreak_db

DISEASE_KEYWORDS = [
    "flu", "influenza", "outbreak", "epidemic", "virus",
    "covid", "dengue", "cholera", "measles", "disease outbreak"
]

def scrape_news():
    api_key = os.getenv("NEWS_API_KEY")
    articles_saved = 0

    for keyword in DISEASE_KEYWORDS:
        url = f"https://newsapi.org/v2/everything?q={keyword}&language=en&sortBy=publishedAt&pageSize=10&apiKey={api_key}"
        response = requests.get(url)
        data = response.json()

        if data.get("status") != "ok":
            print(f"❌ Error for {keyword}:", data.get("message"))
            continue

        for article in data.get("articles", []):
            doc = {
                "title": article.get("title"),
                "description": article.get("description"),
                "content": article.get("content"),
                "source": article.get("source", {}).get("name"),
                "url": article.get("url"),
                "published_at": article.get("publishedAt"),
                "keyword": keyword,
                "scraped_at": datetime.now(timezone.utc)
            }
            db.news_articles.update_one(
                {"url": doc["url"]},
                {"$set": doc},
                upsert=True
            )
            articles_saved += 1

    print(f"✅ Scraped and saved {articles_saved} articles!")
    return articles_saved

if __name__ == "__main__":
    scrape_news()
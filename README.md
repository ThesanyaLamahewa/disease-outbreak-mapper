# 🦠 Disease Outbreak Mapper

A real-time AI-powered disease outbreak monitoring dashboard that scrapes live news, predicts hotspots, and visualizes risk levels on an interactive world map.

🔴 **Live Demo:** [web-production-52fea.up.railway.app](https://web-production-52fea.up.railway.app)

---

## 🚀 Features

- 🗺️ **Interactive World Map** — Real-time hotspot visualization using Leaflet.js with color-coded risk circles
- 📰 **Live News Scraping** — Automatically scrapes disease-related news from 10+ keywords using NewsAPI
- 🤖 **AI Risk Prediction** — Keyword-based NLP scoring engine that classifies regions as HIGH, MEDIUM, or LOW risk
- 📊 **Charts & Analytics** — Bar charts showing risk scores by region using Chart.js
- 📡 **Live News Feed** — Clickable real-time news articles linked to original sources
- 🔄 **Auto-updating Stats** — Live article count, region tracking, and risk distribution

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | MongoDB Atlas (NoSQL) |
| News Data | NewsAPI, BeautifulSoup |
| AI/ML | Keyword NLP, Risk Scoring Engine |
| Frontend | HTML, CSS, JavaScript |
| Map | Leaflet.js |
| Charts | Chart.js |
| Deployment | Railway |

---

## 📁 Project Structure
```
outbreak-mapper/
├── app.py                 # Flask backend & API routes
├── config.py              # Configuration & environment variables
├── requirements.txt       # Python dependencies
├── Procfile               # Deployment configuration
├── scraper/
│   └── news_scraper.py    # NewsAPI scraper
├── models/
│   └── predictor.py       # AI risk prediction engine
└── templates/
    └── index.html         # Frontend dashboard
```

---

## ⚙️ How It Works

1. **News Scraper** fetches articles from NewsAPI using disease keywords (flu, outbreak, epidemic, etc.)
2. **AI Predictor** analyses each article, calculates a risk score based on keyword weights
3. **Risk Scores** are saved to MongoDB and grouped by country
4. **Flask API** serves the data through REST endpoints
5. **Frontend Dashboard** visualizes everything on an interactive map with live charts

---

## 🔧 Run Locally
```bash
# Clone the repo
git clone https://github.com/ThesanyaLamahewa/disease-outbreak-mapper.git
cd disease-outbreak-mapper

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env file
MONGO_URI=your_mongodb_uri
NEWS_API_KEY=your_newsapi_key
SECRET_KEY=your_secret_key

# Run the app
python app.py
```

---

## 📊 API Endpoints

| Endpoint | Description |
|---|---|
| `GET /` | Main dashboard |
| `GET /api/stats` | Article & hotspot statistics |
| `GET /api/hotspots` | Risk scores by country |
| `GET /api/news` | Latest scraped news articles |

---

## 🌍 Risk Level Classification

| Risk Level | Score Range | Color |
|---|---|---|
| 🔴 HIGH | 70 - 100 | Red |
| 🟡 MEDIUM | 40 - 69 | Orange |
| 🟢 LOW | 0 - 39 | Green |

---

## 👩‍💻 Author

**Thesanya Lamahewa**
- GitHub: [@ThesanyaLamahewa](https://github.com/ThesanyaLamahewa)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

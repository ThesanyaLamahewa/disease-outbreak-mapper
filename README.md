# Disease Outbreak Mapper

An AI-powered real-time epidemic monitoring and visualization platform designed to track global disease outbreak trends using live news intelligence, geographic mapping, and automated risk prediction.

Developed as a full-stack data-driven web application, this project demonstrates practical skills in software engineering, data science, API integration, cloud deployment, and real-time analytics.

---

## Overview

Disease Outbreak Mapper collects global disease-related news articles, analyzes outbreak severity using NLP-based keyword scoring, and visualizes high-risk regions through an interactive live dashboard.

The system was designed to address the lack of accessible public tools capable of monitoring outbreak signals in real time before situations escalate.

Key capabilities include:

* Real-time disease news aggregation
* AI-powered outbreak risk classification
* Interactive geographic hotspot mapping
* REST API architecture
* Live dashboard analytics
* Cloud deployment with production hosting

---

## Features

* Automated disease news collection using NewsAPI
* AI-based risk prediction engine
* Interactive hotspot visualization with Leaflet.js
* Real-time dashboard statistics and charts
* MongoDB cloud database integration
* RESTful Flask backend APIs
* Responsive frontend interface
* Production deployment on Railway

---

## Tech Stack

| Category           | Technologies          |
| ------------------ | --------------------- |
| Backend            | Python, Flask         |
| Database           | MongoDB Atlas         |
| Frontend           | HTML, CSS, JavaScript |
| Mapping            | Leaflet.js            |
| Data Visualization | Chart.js              |
| APIs               | NewsAPI               |
| Web Scraping       | BeautifulSoup         |
| Deployment         | Railway               |
| Version Control    | Git & GitHub          |

---

## System Architecture

```text
NewsAPI / Web Sources
            ↓
      Data Collection
            ↓
   NLP Risk Prediction Engine
            ↓
       MongoDB Storage
            ↓
       Flask REST APIs
            ↓
 Interactive Dashboard & Map
```

---

## AI Risk Prediction

The platform uses a keyword-weighted NLP scoring mechanism to estimate outbreak severity levels.

Risk levels are categorized as:

* HIGH
* MEDIUM
* LOW

The prediction engine evaluates:

* outbreak-related terminology,
* article frequency,
* severity indicators,
* country mentions,
* emergency-related language patterns.

---

## Dashboard Components

### Interactive World Map

Displays outbreak hotspots with color-coded markers representing regional risk levels.

### Real-Time Analytics

Live charts and outbreak statistics generated dynamically from incoming data.

### News Intelligence Feed

Continuously updated outbreak-related news articles with geographic tagging.

---

## REST API Endpoints

```http
GET /api/stats
GET /api/hotspots
GET /api/news
```

These endpoints provide live outbreak statistics, hotspot data, and news intelligence for frontend rendering.

---

## Challenges Solved

### DNS Resolution Issues

Implemented custom DNS configuration programmatically to ensure stable API communication during deployment.

### Secure Environment Management

Integrated `.env` configuration locally and Railway environment variables in production to protect API credentials.

### Deployment Constraints

Migrated hosting infrastructure to Railway for scalable and accessible cloud deployment.

### Data Quality Filtering

Improved outbreak relevance using weighted keyword analysis to reduce false-positive news classifications.

---

## Learning Outcomes

This project strengthened practical experience in:

* Full-stack application development
* REST API engineering
* Cloud deployment workflows
* NoSQL database design
* NLP-based data analysis
* Real-time dashboard systems
* Debugging and production troubleshooting
* Version control collaboration using Git and GitHub

---

## Live Deployment

Live Application:
[Disease Outbreak Mapper Live Demo](https://web-production-52fea.up.railway.app?utm_source=chatgpt.com)

GitHub Repository:
[GitHub Repository](https://github.com/ThesanyaLamahewa/disease-outbreak-mapper?utm_source=chatgpt.com)

---

## Installation

```bash
git clone https://github.com/ThesanyaLamahewa/disease-outbreak-mapper.git

cd disease-outbreak-mapper

pip install -r requirements.txt

python app.py
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
NEWS_API_KEY=your_api_key
MONGO_URI=your_mongodb_connection
```

---

## Future Improvements

* Machine learning-based outbreak forecasting
* Historical outbreak trend analysis
* User alert and notification system
* Multi-language news processing
* Advanced geospatial clustering
* Public health reporting integration

---

## Author

Thesanya Lamahewa

Focused on building impactful AI and data-driven solutions combining software engineering, analytics, and real-world problem solving.

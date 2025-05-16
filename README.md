# News Scraper and Sentiment Analyzer

This is a modular Python project to scrape and analyze leftist media articles from sources like Jacobin, Common Dreams, and Democracy Now!.

---

## Features
- Modular scrapers for different sources
- Sentiment analysis on headlines and article content
- Easily expandable for new sites or analysis tools
- Optional bot (Discord, Telegram, Mastodon) for auto-sharing content or send SMS with REST

---

## How to Use

```bash
# Clone repository and enter folder
git clone https://github.com/tabriz-s/web-scraper.git
cd web-scraper

# Set up virtual environment
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

# Run scraper
python scraper/jacobin_scraper.py
```

---

## TODO
- Common Dreams and Democracy Now! scrapers
- Sentiment analysis pipeline
- CLI or dashboard for viewing data
- Bot for posting or sending SMS with REST API
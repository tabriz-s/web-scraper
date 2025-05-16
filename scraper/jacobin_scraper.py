from base_scraper import BaseScraper
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

class JacobinScraper(BaseScraper):
    def __init__(self, base_url='https://jacobin.com'):
        super().__init__(base_url)
        self.base_url = base_url
        # self.articles = []

    def scrape(self):
        response = requests.get(self.base_url)
        if response.status_code != 200:
            print(f"Failed to fetch page: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')

        data = []

        for article in articles:
            # Extract title
            title_tag = article.find('h2') or article.find('h3')
            title = title_tag.get_text(strip=True) if title_tag else None

            # Extract link
            link_tag = title_tag.find('a') if title_tag else None
            link = self.base_url + link_tag['href'] if link_tag and link_tag.get('href') else None

            # Extract date
            time_tag = article.find('time')
            date_str = time_tag['datetime'] if time_tag and time_tag.get('datetime') else None
            try:
                pub_date = datetime.fromisoformat(date_str)
            except:
                pub_date = None

            # Extract author
            author_tag = article.find('a', class_='hm-dg__author-link')
            author = author_tag.get_text(strip=True) if author_tag else None

            # Extract summary
            summary_tag = article.find('p', class_="hm-dg__summary")
            summary = summary_tag.get_text(strip=True) if summary_tag else None
            
            if title and link:
                data.append({
                    "title": title,
                    "url": link,
                    "date": pub_date,
                    "author": author,
                    "summary": summary,
                    "source": "Jacobin"
                })

        # Save
        df = pd.DataFrame(data)
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
        os.makedirs('data/raw', exist_ok=True)
        df.to_csv(f'data/raw/jacobin_{timestamp}.csv', index=False)
        print(f"Scraped {len(df)} articles from Jacobin.")
        

    # def save_to_csv(self, articles, filename='jacobin_articles.csv'):
    #     if not articles:
    #         print("No articles to save.")
    #         return
        
    #     # Save the scraped articles to a CSV file
    #     df = pd.DataFrame(articles)
    #     out_path = os.path.join('data', filename)
    #     os.makedirs(os.path.dirname(out_path), exist_ok=True)
    #     df.to_csv(out_path, index=False)
    #     print(f"Scraped {len(df)} articles from Jacobin.")
    

if __name__ == '__main__':
    scraper = JacobinScraper()
    scraper.scrape()
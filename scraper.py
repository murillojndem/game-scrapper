import requests
from bs4 import BeautifulSoup
import urllib.parse
import subprocess
import re

class GameScraper:
    def __init__(self, existing_terms):
        self.existing_terms = existing_terms
        self.chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        self.urls = [
            'https://1337x.to/popular-games',
            'https://1337x.to/popular-games-week',
            'https://1337x.to/trending/d/games/',
            'https://1337x.to/trending/w/games/',
            'https://1337x.to/top-100-games'
        ]

    def scrape_game_terms(self):
        new_searched_terms = set()
        for url in self.urls:
            new_terms = self._scrape_url(url)
            new_searched_terms.update(new_terms)
        return new_searched_terms

    def _scrape_url(self, url):
        new_terms = set()
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        featured_div = soup.find('div', class_='featured-list')
        game_links = featured_div.find_all('a') if featured_div else []

        for link in game_links:
            if link.get('href', '').startswith('/user'):
                continue

            full_game_name = link.get_text().strip()
            if not full_game_name:
                continue

            game_name = full_game_name.split(' (')[0]
            game_name = re.sub(r'\bv\d+(\.\d+)*', '', game_name).strip()
            game_name = game_name.replace('Update', '').strip()
            search_term = game_name + " gameplay"

            if search_term in self.existing_terms:
                continue
            else:
                self.existing_terms.add(search_term)
                new_terms.add(search_term)

                print(f"Pesquisando por: {search_term}")
                search_query = urllib.parse.quote(search_term)
                youtube_search_url = f"https://www.youtube.com/results?search_query={search_query}"
                subprocess.Popen([self.chrome_path, youtube_search_url])

        return new_terms

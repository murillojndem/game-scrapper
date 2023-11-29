import requests
from bs4 import BeautifulSoup
import urllib.parse
import subprocess
import re

# Caminho para o arquivo .txt onde os termos de pesquisa serão salvos
search_terms_file = 'E:\\Projetos\\Python\\game-scraper\\searched_terms.txt'

# Carregar termos de pesquisa já realizados
searched_terms = set()
try:
    with open(search_terms_file, 'r', encoding='utf-8') as file:
        searched_terms = set(file.read().splitlines())
except FileNotFoundError:
    pass

# Conjunto para armazenar os novos termos pesquisados nesta execução
new_searched_terms = set()

# Lista de URLs para raspar
urls = [
    'https://1337x.to/popular-games',
    'https://1337x.to/popular-games-week',
    'https://1337x.to/trending/d/games/',
    'https://1337x.to/trending/w/games/',
    'https://1337x.to/top-100-games'
]

# Caminho para o executável do Chrome
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

for url in urls:
    # Busca o conteúdo da página web
    response = requests.get(url)
    response.raise_for_status()

    # Analisa o conteúdo HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra a div com a classe 'featured-list' e depois encontra todas as tags <a> dentro desta div
    featured_div = soup.find('div', class_='featured-list')
    game_links = featured_div.find_all('a') if featured_div else []

    # Itera sobre cada link
    for link in game_links:
        # Verifica se o atributo 'href' começa com '/user'
        if link.get('href', '').startswith('/user'):
            continue

        full_game_name = link.get_text().strip()

        # Pula nomes de jogos vazios
        if not full_game_name:
            continue

        # Extrai o nome antes do parêntese (se houver)
        game_name = full_game_name.split(' (')[0]

        # Remove qualquer parte que comece com 'v' seguido por um número
        game_name = re.sub(r'\bv\d+(\.\d+)*', '', game_name).strip()

        # Remove a palavra "update"
        game_name = game_name.replace('Update', '').strip()

        # Adiciona " gameplay" ao nome do jogo
        search_term = game_name + " gameplay"

        # Verifica se este termo de pesquisa já foi pesquisado
        if search_term in searched_terms:
            continue
        else:
            # Adiciona o termo ao conjunto de termos pesquisados
            searched_terms.add(search_term)
            new_searched_terms.add(search_term)

            # Imprime o nome do jogo sendo pesquisado
            print(f"Pesquisando por: {search_term}")

            # Constrói a URL de pesquisa do YouTube
            search_query = urllib.parse.quote(search_term)
            youtube_search_url = f"https://www.youtube.com/results?search_query={search_query}"

            # Abre a pesquisa em uma nova janela do Chrome usando subprocess
            subprocess.Popen([chrome_path, youtube_search_url])

# Verifica se nenhum termo novo foi pesquisado
if not new_searched_terms:
    print("Todos os termos já foram pesquisados anteriormente. Não há nenhum termo novo para pesquisar.")

# Salvar os novos termos de pesquisa no arquivo .txt
with open(search_terms_file, 'a', encoding='utf-8') as file:
    for term in new_searched_terms:
        file.write(term + '\n')

from scraper import GameScraper
from utils import SearchTermsFileManager

def main():
    search_terms_file = 'E:\\Projetos\\Python\\game-scraper\\searched_terms.txt'
    file_manager = SearchTermsFileManager(search_terms_file)

    scraper = GameScraper(file_manager.load_searched_terms())

    new_searched_terms = scraper.scrape_game_terms()

    if new_searched_terms:
        file_manager.save_searched_terms(new_searched_terms)
        print("Novos termos pesquisados e salvos.")
    else:
        print("Não há novos termos para pesquisar.")

if __name__ == "__main__":
    main()

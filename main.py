import logging
from scraper import GameScraper
from utils import SearchTermsFileManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    search_terms_file = 'E:\\Projetos\\Python\\game-scraper\\searched_terms.txt'
    file_manager = SearchTermsFileManager(search_terms_file)

    try:
        scraper = GameScraper(file_manager.load_searched_terms())
        new_searched_terms = scraper.scrape_game_terms()

        if new_searched_terms:
            file_manager.save_searched_terms(new_searched_terms)
            logging.info("Novos termos pesquisados e salvos.")
        else:
            logging.info("Não há novos termos para pesquisar.")
    except Exception as e:
        logging.error(f"Erro durante a execução do script: {e}")

if __name__ == "__main__":
    main()

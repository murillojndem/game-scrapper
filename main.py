from scraper import scrape_game_terms
from utils import load_searched_terms, save_searched_terms

def main():
    search_terms_file = 'E:\\Projetos\\Python\\game-scraper\\searched_terms.txt'
    searched_terms = load_searched_terms(search_terms_file)

    new_searched_terms = scrape_game_terms(searched_terms)

    if new_searched_terms:
        save_searched_terms(search_terms_file, new_searched_terms)
        print("Novos termos pesquisados e salvos.")
    else:
        print("Não há novos termos para pesquisar.")

if __name__ == "__main__":
    main()

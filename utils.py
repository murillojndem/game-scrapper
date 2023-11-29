import logging

class SearchTermsFileManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_searched_terms(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                return set(file.read().splitlines())
        except FileNotFoundError:
            logging.warning("Arquivo de termos pesquisados não encontrado. Iniciando com um conjunto vazio.")
            return set()

    def save_searched_terms(self, terms):
        try:
            with open(self.filepath, 'a', encoding='utf-8') as file:
                for term in terms:
                    file.write(term + '\n')
        except IOError as e:
            logging.error(f"Erro ao salvar termos pesquisados: {e}")

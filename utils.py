class SearchTermsFileManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_searched_terms(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                return set(file.read().splitlines())
        except FileNotFoundError:
            return set()

    def save_searched_terms(self, terms):
        with open(self.filepath, 'a', encoding='utf-8') as file:
            for term in terms:
                file.write(term + '\n')

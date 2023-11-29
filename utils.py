def load_searched_terms(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        return set()

def save_searched_terms(filename, terms):
    with open(filename, 'a', encoding='utf-8') as file:
        for term in terms:
            file.write(term + '\n')

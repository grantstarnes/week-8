from collections import defaultdict
import numpy as np

class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    def get_term_dict(self):

        term_dict = defaultdict(list)

        if isinstance(self.corpus, str):
            tokens = self.corpus.split()
        else:
            tokens = self.corpus
        
        for i in range(len(tokens) - 1):
            current_word = tokens[i]
            following_word = tokens[i + 1]
            term_dict[current_word].append(following_word)

        self.term_dict = dict(term_dict)

        return self.term_dict


    def generate(self, seed_term=None, term_count=15):

        if seed_term is None:
            current_word = np.random.choice(list(self.term_dict.keys()))
        else:
            if seed_term not in self.term_dict:
                raise ValueError(f"Seed term '{seed_term}' not in term_dict")
            current_word = seed_term

        selected_word = [current_word]

        for _ in range(term_count - 1):
            next_words = self.term_dict.get(current_word)
            if not next_words:
                current_word = np.random.choice(list(self.term_dict.keys()))
            else:
                current_word = np.random.choice(next_words)
            selected_word.append(current_word)

        return " ".join(selected_word)
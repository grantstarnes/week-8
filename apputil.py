from collections import defaultdict


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

        # your code here ...

        return None
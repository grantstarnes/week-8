from collections import defaultdict


class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    def get_term_dict(self):

        term_dict = defaultdict(list)

        self.term_dict = {}

        return None


    def generate(self, seed_term=None, term_count=15):

        # your code here ...

        return None
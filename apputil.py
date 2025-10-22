from collections import defaultdict
import numpy as np

class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None

    def get_term_dict(self):
        '''
        This method get_term_dict creates a dictionary where each key is a unique
        token from the defined corpus. The value for each key is a list of following
        words that directly follow the key/token. This method finally then returns a 
        dictionary with the token words and their list of following words for every word.
        '''

        # Creates a dictionary where all keys have an empty list as the value
        term_dict = defaultdict(list)

        # If the corpus taken in is a string, we will split it into a list of words
        # Else, is if the corpus taken in is a list of tokens as is
        if isinstance(self.corpus, str):
            tokens = self.corpus.split()
        else:
            tokens = self.corpus
        
        # We will iterate through each token, and for each token, we will append
        # each word that follows the token to the corresponding list for the values
        # of each token
        for i in range(len(tokens) - 1):
            current_word = tokens[i]
            following_word = tokens[i + 1]
            term_dict[current_word].append(following_word)

        # This just converts term_dict to a dictionary before getting the output
        self.term_dict = dict(term_dict)

        # Returns the dictionary
        return self.term_dict


    def generate(self, seed_term=None, term_count=15):
        '''
        This generate method utilizes the term_dict from the get_term_dict method
        to generate a random sequence of words using numpy (np.random.choice).
        It takes in a possible seed word, and if one isn't provided, it will 
        select a random seed word instead. After that, each following word in the 
        string is chosen at random as well based on the words that typically would
        follow the current_word.
        '''

        # Selects the starting word whether it's the provided seed or randomized seed
        if seed_term is None:
            current_word = np.random.choice(list(self.term_dict.keys()))
        else:
            # Makes sure the provided seed is in the term_dict, throws a ValueError if not
            if seed_term not in self.term_dict:
                raise ValueError(f"Seed term '{seed_term}' not in term_dict")
            current_word = seed_term

        selected_word = [current_word]

        # Uses a for loop to randomly generate the remaining words
        for _ in range(term_count - 1):

            # Gets the list from term_dict of the possible words that follow
            next_words = self.term_dict.get(current_word)

            if not next_words:

                # If the selected word doesn't have a following word, it will randomize and select a new word from term_dict
                current_word = np.random.choice(list(self.term_dict.keys()))
            else:
                # Else, it will randomly select the next word from the list of following words
                current_word = np.random.choice(next_words)
            
            # Appends the chosen word to selected_word
            selected_word.append(current_word)

        # Joins all of the words into one single combined string, and returns this string
        return " ".join(selected_word)
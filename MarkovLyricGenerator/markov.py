from random import randint
# Markov chain is basically just a probability flowchart based on frequency from one word to the next set,
# then the next set, etc.
class MarkovLyrics:
    # self.chain = {
    #    "baby": ["play", "crawls", "sleeps", "plays"],
    #    "plays": ["toy", "food"]
    # }
    def __init__(self):
        # creating a dictionary
        self.chain = {}

    def populateMarkovChain(self, lyrics):
        for line in lyrics:
            words = line.split(" ")

            for i in range(len(words) - 1):
                word = words[i]

                # If word already exists, then get next word and append
                if word in self.chain:
                    next_word = words[i + 1]
                    self.chain[word].append(next_word)
                else:
                    next_word = words[i + 1]
                    self.chain[word] = [next_word]

    def generateLyrics(self, length=500):
        n = len(self.chain)

        # Select random index from 0 and max
        start_index = randint(0, n-1)
        keys = list(self.chain.keys())
        # .title capitalizes first letter of word
        current_word = keys[start_index].title()

        lyrics = current_word + " "

        for _ in range(length):
            if current_word not in self.chain:
                lyrics += "\n"
                next_index = randint(0, n - 1)
                current_word = keys[next_index]
            else:
                next_words = self.chain[current_word]
                next_index = randint(0, len(next_words) - 1)
                next_word = next_words[next_index]
                lyrics += next_word + ' '
                current_word = next_word

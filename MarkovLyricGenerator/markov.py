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

data = ["I am avi", "I am an engineer", "I like to code"]
m = MarkovLyrics()
m.populateMarkovChain(data)
print(m.chain)
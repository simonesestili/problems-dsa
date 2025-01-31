class StreamChecker:
    def __init__(self, words):
        self.stream = []
        self.trie = Trie()
        for word in set(words):
            self.trie.insert(word[::-1])

    def query(self, letter):
        self.stream.append(letter)
        curr = self.trie
        for i in range(len(self.stream) - 1, -1, -1):
            let = self.stream[i]
            if let not in curr:
                return False
            curr = curr[let]
            if '*' in curr:
                return True
        return False

class Trie(dict):
    def insert(self, word):
        curr = self
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['*'] = True

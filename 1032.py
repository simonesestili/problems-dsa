class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        # This denotes that the current node is the end of word
        curr['*'] = True    

class StreamChecker:
    def __init__(self, words):
        self.stream = []
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter):
        last = len(self.stream)
        self.stream.append(letter)
        # Check if suffix of stream is in words
        curr = self.trie.root
        while last >= 0:
            letter = self.stream[last]
            if letter not in curr:
                return False
            curr = curr[letter]
            if '*' in curr:
                return True
            last -= 1
        return False    

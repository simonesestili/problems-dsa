class Trie(dict):
    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr: curr[c] = {}
            curr = curr[c]
        curr['*'] = {}

    def search(self, word, node=None, i=0):
        if node is None:
            node = self
        if i == len(word):
            return '*' in node
        if word[i] == '.':
            return any(self.search(word, node[c], i + 1) for c in node)
        return word[i] in node and self.search(word, node[word[i]], i + 1)

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        self.trie.insert(word)

    def search(self, word):
        return self.trie.search(word)

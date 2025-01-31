class Trie:

    def __init__(self):
        self.trie = {}
        self.trie['*'] = {}

    def insert(self, word: str) -> None:
        self.ins(word, 0, self.trie['*'])

    def ins(self, word, idx, curr):
        if idx == len(word):
            curr['*'] = True
            return
        if word[idx] not in curr:
            curr[word[idx]] = {}
        self.ins(word, idx + 1, curr[word[idx]])    
    
    def search(self, word: str) -> bool:
        return self.exists(word, 0, self.trie['*'])

    def exists(self, word, idx, curr):
        if idx == len(word):
            return '*' in curr
        if word[idx] not in curr:
            return False
        return self.exists(word, idx + 1, curr[word[idx]])

    def startsWith(self, prefix: str) -> bool:
        return self.starts(prefix, 0, self.trie['*'])

    def starts(self, prefix, idx, curr):
        if idx == len(prefix):
            return True

        if prefix[idx] not in curr:
            return False
        return self.starts(prefix, idx + 1, curr[prefix[idx]])

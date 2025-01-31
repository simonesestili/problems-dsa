class Trie:
    def __init__(self):
        self.chars = {}
        
    def insert(self, word):
        curr = self.chars
        for c in word:
            if c not in curr: curr[c] = {}
            curr = curr[c]
        curr['*'] = True

    def prefix(self, word):
        curr, res = self.chars, []
        for c in word:
            if c not in curr: break 
            curr = curr[c]
            res.append(c)
            if '*' in curr:
                return ''.join(res)
        return None

class Solution:
    def replaceWords(self, roots, sentence):
        trie = Trie()
        for root in roots: trie.insert(root)
        return ' '.join(trie.prefix(word) or word for word in sentence.split())


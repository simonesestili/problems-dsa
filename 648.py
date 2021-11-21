class Trie:
    def __init__(self):
        self.chars = {}
        
    def insert(self, word):
        curr = self.chars
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['*'] = True

class Solution:
    def replaceWords(self, dictionary, sentence):
        words, trie = sentence.split(), Trie()
        for root in dictionary:
            trie.insert(root)
        for i, word in enumerate(words):
            curr = trie.chars
            for j, char in enumerate(word):
                if char not in curr:
                    break
                curr = curr[char]
                if '*' in curr:
                    words[i] = word[:j + 1]
                    break
        return ' '.join(words)

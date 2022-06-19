class Solution:
    def suggestedProducts(self, products, search):
        trie = TrieNode()
        for word in sorted(products):
            trie.insert(word)

        ans = [[] for _ in search]
        for i, c in enumerate(search):
            if c not in trie: break
            ans[i] = trie[c].suggested
            trie = trie[c]

        return ans

class TrieNode(dict):
    def __init__(self):
        self.suggested = []

    def insert(self, word):
        curr = self
        for c in word:
            curr = curr.setdefault(c, TrieNode())
            if len(curr.suggested) < 3:
                curr.suggested.append(word)

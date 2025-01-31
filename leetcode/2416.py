class Node:
    def __init__(self):
        self.cnt = 0
        self.children = {}

class Solution:
    def sumPrefixScores(self, words):
        trie = Node()
        for word in words:
            curr = trie
            for c in word:
                if c not in curr.children: curr.children[c] = Node()
                curr = curr.children[c]
                curr.cnt += 1
        ans = [0] * len(words)
        for i, word in enumerate(words):
            curr = trie
            for c in word:
                if c not in curr.children: break
                curr = curr.children[c]
                ans[i] += curr.cnt
        return ans

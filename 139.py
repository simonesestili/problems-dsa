class Trie(dict):
    def insert(self, word):
        curr = self
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['*'] = True

class Solution:
    def wordBreak(self, s, words):
        n = len(s)
        trie = Trie()
        for word in words:
            trie.insert(word)
        dp = [False] * n + [True]

        for i in range(n - 1, -1, -1):
            curr = trie
            for j in range(i, n):
                if s[j] not in curr:
                    break
                curr = curr[s[j]]
                if '*' in curr:
                    dp[i] |= dp[j + 1]

        return dp[0]

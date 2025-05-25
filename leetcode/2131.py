class Solution:
    def longestPalindrome(self, words):
        cnts = Counter(words)
        return 4 * sum(min(cnts[w], cnts[w[::-1]]) if w[0] != w[1] else cnts[w] // 2 for w in cnts if w[0] <= w[1]) + 2 * any(w[0] == w[1] and cnts[w] & 1 for w in cnts)

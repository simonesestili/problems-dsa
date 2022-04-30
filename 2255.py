class Solution:
    def countPrefixes(self, words, s):
        return sum(s.startswith(word) for word in words)

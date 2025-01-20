class Solution:
    def prefixCount(self, words, pref):
        return sum(w.startswith(pref) for w in words)

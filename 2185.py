class Solution:
    def prefixCount(self, words, pref):
        count = 0
        for word in words:
            count += word.startswith(pref)
        return count

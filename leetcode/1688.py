class Solution:
    def numberOfMatches(self, n):
        matches = 0

        while n != 1:
            matches += n >> 1
            n = (n + 1) >> 1 if n & 1 else n >> 1

        return matches

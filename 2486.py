class Solution:
    def appendCharacters(self, s, t):
        n, m, i = len(s), len(t), 0
        for j in range(m):
            while i < n and s[i] != t[j]: i += 1 
            if i == n: return m - j
            i += 1
        return 0


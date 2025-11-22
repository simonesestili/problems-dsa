class Solution:
    def countPalindromicSubsequence(self, s):
        l, r = {}, {}
        for i, c in enumerate(s): l[c], r[c] = l.get(c, i), i
        return sum(len(set(s[l[c]+1:r[c]])) for c in l if l[c] < r[c])

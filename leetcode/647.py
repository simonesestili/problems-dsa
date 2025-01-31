class Solution:
    def countSubstrings(self, s):
        n, count = len(s), 0

        def expand(l, r):
            res = 0
            while l >= 0 and r < n and s[l] == s[r]:
                l, r = l - 1, r + 1
                res += 1
            return res

        return sum(expand(i, i) + expand(i, i + 1) for i in range(n))

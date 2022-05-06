class Solution:
    def findPermutation(self, s):
        n, i = len(s), 0
        perm = list(range(1, n + 2))

        def rev(l, r):
            while l < r:
                perm[l], perm[r] = perm[r], perm[l]
                l, r = l + 1, r - 1

        while i < n:
            left = i
            while i < n and s[i] == 'D': i += 1
            rev(left, i)
            i += 1

        return perm




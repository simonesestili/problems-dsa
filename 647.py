class Solution:
    def countSubstrings(self, s):
        n, count = len(s), 1

        def expand(l, r):
            res = 0
            while l >= 0 and r < n and s[l] == s[r]:
                l, r = l - 1, r + 1
                res += 1
            return res

        for mid in range(n - 1):
            count += expand(mid, mid) # odd lengthed
            count += expand(mid, mid + 1) # even lengthed

        return count

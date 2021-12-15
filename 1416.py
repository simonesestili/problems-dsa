class Solution:
    def numberOfArrays(self, s, k):
        n, M = len(s), pow(10, 9) + 7

        @cache
        def dp(i):
            if i >= n or s[i] == '0': return int(i >= n)
            ans, curr, j = 0, 0, i
            while j < n:
                curr = curr * 10 + int(s[j])
                if curr > k: break
                ans = (ans + dp(j + 1)) % M
                j += 1
            return ans

        return dp(0)

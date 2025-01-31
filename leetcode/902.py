class Solution:
    def atMostNGivenDigitSet(self, digs, n):
        n, m, digs, less, k = str(n), len(str(n)), set(digs), [0] * 10, len(digs)
        for i in range(1, 10):
            less[i] = less[i - 1] + (str(i - 1) in digs)
        dp = [0] * m
        dp[-1] = less[int(n[-1])] + (n[-1] in digs)
        for i in range(m - 2, -1, -1):
            dp[i] = less[int(n[i])] * pow(k, m - i - 1)
            if n[i] in digs: dp[i] += dp[i + 1]

        extra = m - 1 if k == 1 else (1 - pow(k, m)) // (1 - k) - 1
        return dp[0] + extra

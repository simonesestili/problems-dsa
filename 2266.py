MOD = 10 ** 9 + 7
mapping = [0,0,3,3,3,3,3,4,3,4]
class Solution:
    def countTexts(self, s):
        n, s = len(s), list(map(int, s))

        dp = [0] * n + [1]
        for i in range(n - 1, -1, -1):
            for j in range(min(mapping[s[i]], n - i)):
                if s[i+j] != s[i]: break
                dp[i] = (dp[i] + dp[i+j+1]) % MOD

        return dp[0]

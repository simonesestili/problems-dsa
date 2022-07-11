MOD = 10 ** 9 + 7
class Solution:
    def idealArrays(self, n, k):
        ans, prev = k, [1] * (k + 1)
        for count in range(2, 15):
            dp = [0] * (k + 1)
            for end in range(1, k + 1):
                for mul in range(end * 2, k + 1, end):
                    dp[mul] = (dp[mul] + prev[end]) % MOD
            ans = (ans + sum(dp) % MOD * math.comb(n - 1, count - 1)) % MOD
            prev = dp
        return ans

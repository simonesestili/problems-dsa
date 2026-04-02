class Solution:
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        memo = [[[None] * 3 for _ in range(n)] for _ in range(m)]

        def dp(r, c, k):
            if r >= m or c >= n:
                return -inf
            if memo[r][c][k] is None:
                if (r, c) == (m-1, n-1):
                    ans = max(coins[r][c], 0 if k else -inf)
                else:
                    ans = coins[r][c] + max(dp(r+1, c, k), dp(r, c+1, k))
                    if coins[r][c] < 0 and k:
                        ans = max(ans, dp(r+1, c, k-1), dp(r, c+1, k-1))
                memo[r][c][k] = ans
            return memo[r][c][k]

        return dp(0, 0, 2)

class Solution:
    def change(self, amount, coins):
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]
        dp[0][0] = 1
        
        for amt in range(amount + 1):
            for i in range(n):
                dp[i][amt] += 0 if amt - coins[i] < 0 else dp[i][amt - coins[i]]
                dp[i][amt] += 0 if not i else dp[i-1][amt]

        return dp[-1][-1]

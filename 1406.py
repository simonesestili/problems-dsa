class Solution:
    def stoneGameIII(self, stones):
        n = len(stones)
        dp = [float('-inf')] * (n + 1)
        dp[-1] = 0
        for i in range(n - 1, -1, -1):
            curr = 0
            for j in range(3):
                if i + j >= n: break
                curr += stones[i + j]
                dp[i] = max(dp[i], curr - dp[i + j + 1])

        return 'Alice' if dp[0] > 0 else 'Bob' if dp[0] < 0 else 'Tie'

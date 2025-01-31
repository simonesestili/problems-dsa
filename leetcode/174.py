class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[9e9 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[-1][n - 1], dp[m - 1][-1] = 1, 1
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                dp[row][col] = max(min(dp[row + 1][col], dp[row][col + 1]) - dungeon[row][col], 1)
        return dp[0][0]        

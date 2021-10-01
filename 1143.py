class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for col in range(m - 1, -1, -1):
            for row in range(n - 1, -1, -1):
                if text1[col] == text2[row]:
                    dp[row][col] = 1 + self.get(dp, row + 1, col + 1)
                else:
                    dp[row][col] = max(self.get(dp, row + 1, col), self.get(dp, row, col + 1))
        return dp[0][0]

    def get(self, dp, row, col):
        if row < 0 or col < 0 or row >= len(dp) or col >= len(dp[0]):
            return 0
        return dp[row][col]

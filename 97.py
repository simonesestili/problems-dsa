class Solution:
    def isInterleave(self, s1, s2, s3):
        m, n = len(s1), len(s2)
        if m + n != len(s3): return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i + j]:
                    dp[i][j] |= dp[i + 1][j]
                if j < n and s2[j] == s3[i + j]:
                    dp[i][j] |= dp[i][j + 1]
        return dp[0][0]

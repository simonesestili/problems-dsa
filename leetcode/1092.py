class Solution:
    def shortestCommonSupersequence(self, a, b):
        m, n = len(a), len(b)
        dp = [[m - y if x == n else n - x for x in range(n + 1)] for y in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if a[i] == b[j]: dp[i][j] = 1 + dp[i+1][j+1]
                else: dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1])

        ans = []
        i = j = 0
        while (i, j) != (m, n):
            if i < m and j < n and a[i] == b[j]:
                ans.append(a[i])
                i, j = i + 1, j + 1
            elif i == m or j != n and dp[i][j+1] < dp[i+1][j]:
                ans.append(b[j])
                j += 1
            else:
                ans.append(a[i])
                i += 1

        return ''.join(ans)

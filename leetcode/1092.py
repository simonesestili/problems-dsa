class Solution:
    def shortestCommonSupersequence(self, a, b):
        m, n = len(a), len(b)

        dp = [[m - i if j == n else n - j for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = 1 + (dp[i+1][j+1] if a[i] == b[j] else min(dp[i+1][j], dp[i][j+1]))

        ans = []
        i = j = 0
        while (i, j) != (m, n):
            if i < m and j < n and a[i] == b[j]:
                ans.append(a[i])
                i += 1
                j += 1
            elif j == n or i < m and dp[i+1][j] < dp[i][j+1]:
                ans.append(a[i])
                i += 1
            else:
                ans.append(b[j])
                j += 1

        return ''.join(ans)

class Solution:
    def mctFromLeafValues(self, arr):
        n = len(arr)
        most = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                most[i][j] = max(arr[j], 0 if not j else most[i][j-1])
        
        @cache
        def dp(i, j):
            if i == j: return 0
            ans = float('inf')
            for k in range(i, j):
                ans = min(ans, most[i][k] * most[k+1][j] + dp(i, k) + dp(k + 1, j))
            return ans

        return dp(0, len(arr) - 1)

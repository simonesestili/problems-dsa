class Solution:
    def gridGame(self, grid):
        n = len(grid[0])
        left, right = [0] * n, [0] * n
        for i in range(1, n):
            left[i] = left[i - 1] + grid[1][i - 1]
            right[n - 1 - i] = right[n - i] + grid[0][n - i]
        ans = float('inf')
        for i in range(n):
            ans = min(ans, max(left[i], right[i]))
        return ans


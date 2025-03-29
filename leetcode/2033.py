class Solution:
    def minOperations(self, grid, x):
        m, n = len(grid), len(grid[0])
        vals = sorted(grid[r][c] for c in range(n) for r in range(m))
        med = vals[m*n//2]

        ans = 0
        for r in range(m):
            for c in range(n):
                ops, rem = divmod(abs(grid[r][c] - med), x)
                if rem: return -1
                ans += ops

        return ans

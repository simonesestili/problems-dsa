class Solution:
    def gridGame(self, grid):
        ans, prefix, suffix = inf, 0, sum(grid[0])
        for i in range(len(grid[0])):
            suffix -= grid[0][i]
            ans = min(ans, max(prefix, suffix))
            prefix += grid[1][i]

        return ans

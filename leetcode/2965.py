class Solution:
    def findMissingAndRepeatedValues(self, grid):
        ans, n = [-1, -1], len(grid)
        cnts = Counter(grid[i // n][i % n] for i in range(n * n))
        for x in range(1, n * n + 1):
            if cnts[x] == 2: ans[0] = x
            if cnts[x] == 0: ans[1] = x
        return ans

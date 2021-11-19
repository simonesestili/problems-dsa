class Solution:
    def uniquePaths(self, m, n):
        ways = [[0] * n for _ in range(m)]
        ways[0][0] = 1
        for row in range(m):
            for col in range(n):
                left = 0 if not col else ways[row][col - 1]
                top = 0 if not row else ways[row - 1][col]
                ways[row][col] += left + top
        return ways[-1][-1]

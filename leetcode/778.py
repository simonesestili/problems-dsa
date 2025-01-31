class DSU:
    def __init__(self, n):
        self.reps = [i for i in range(n)]
        self.ranks = [1] * n

    def find(self, n):
        while self.reps[n] != n:
            n = self.reps[n]
        return n

    def union(self, a, b):
        a_rep, b_rep = self.find(a), self.find(b)
        if self.ranks[a_rep] > self.ranks[b_rep]:
            self.reps[b_rep] = a_rep
            self.ranks[a_rep] += self.ranks[b_rep]
        else:
            self.reps[a_rep] = b_rep
            self.ranks[b_rep] += self.ranks[a_rep]

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        dsu = DSU(n * n)
        heights = {}
        for row in range(n):
            for col in range(n):
                heights[grid[row][col]] = (row, col)

        dirs = [0, 1, 0, -1, 0]
        for t in range(n * n):
            row, col = heights[t]
            for i in range(4):
                drow, dcol = row + dirs[i], col + dirs[i + 1]
                if drow >= 0 and dcol >= 0 and drow < n and dcol < n and grid[drow][dcol] < t:
                    dsu.union(row * n + col, drow * n + dcol)
            if dsu.find(0) == dsu.find(n * n - 1):
                return t

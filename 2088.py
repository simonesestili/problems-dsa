class Solution:
    def countPyramids(self, grid):
        self.grid, self.count = grid, 0
        self.prefixSuffix()
        self.countFromBase()
        self.countFromBase(True)
        return self.count

    def countFromBase(self, inverse=False):
        m, n = len(self.grid), len(self.grid[0])
        for col in range(n):
            prev_base = 0
            for i in (range(m - 1, -1, -1) if inverse else range(m)):
                base = 0 if not self.grid[i][col] else min(self.prefix[i][col], self.suffix[i][col]) * 2 + 1
                if base > prev_base: base = prev_base + 2 if prev_base else 1
                self.count += base // 2
                prev_base = base

    def prefixSuffix(self):
        m, n = len(self.grid), len(self.grid[0])
        self.prefix, self.suffix = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
        for row in range(m):
            curri = currj = 0
            for i in range(n):
                j = n - 1 - i
                self.prefix[row][i] = curri
                self.suffix[row][j] = currj
                if self.grid[row][i]: curri += 1
                else: curri = 0
                if self.grid[row][j]: currj += 1
                else: currj = 0

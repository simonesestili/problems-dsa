class Solution:
    def countPyramids(self, grid):
        self.grid, self.count = grid, 0
        # Initialize prefix and suffix grids
        # prefix[i][j] = number of consecutive ones to the left of grid[i][j]
        # suffix[i][j] = number of consecutive ones to the right of grid[i][j]
        self.prefixSuffix()
        # Count all pyramids
        self.countFromBase()
        # Count all inverse pyramids
        self.countFromBase(True)
        return self.count

    def countFromBase(self, inverse=False):
        m, n = len(self.grid), len(self.grid[0])
        # traverse column by column each time considering each row as the base of some pyramids
        # that are centered at the current column
        # the number of pyramids starting at some "complete" base of length n is (n - 1) // 2
        for col in range(n):
            # previous "complete" base size
            prev_base = 0
            for i in (range(m - 1, -1, -1) if inverse else range(m)):
                # minimum "radius" of the base =  min(self.prefix[i][col], self.suffix[i][col])
                # base size  = 2 * radius + 1
                base = 0 if not self.grid[i][col] else min(self.prefix[i][col], self.suffix[i][col]) * 2 + 1
                # if the previous base is not large enough to make the 
                # current base "complete" then decrease the current base's length accordingly
                if base > prev_base: base = prev_base + 2 if prev_base else 1
                # for a pyramid with a base of length n we can make (n - 1) // 2 pyramids 
                # that start with the same base row
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

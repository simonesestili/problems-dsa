class Solution:
    def possibleToStamp(self, mat, h, w):
        m, n = len(mat), len(mat[0])
        self.make_prefix(mat, 1)
        for row in range(m):
            for col in range(n):
                if mat[row][col]: continue
                i, j = row + h - 1, col + w - 1
                if i >= m or j >= n: continue
                if not self.query(row, col, i, j):
                    mat[row][col] = -1
        self.make_prefix(mat, -1)
        for row in range(m):
            for col in range(n):
                if mat[row][col]: continue
                i, j = max(0, row - h + 1), max(0, col - w + 1)
                if not self.query(i, j, row, col): return False
        return True

    def query(self, r1, c1, r2, c2):
        total = self.prefix[r2][c2]
        left = 0 if not c1 else self.prefix[r2][c1 - 1]
        top = 0 if not r1 else self.prefix[r1 - 1][c2]
        extra = 0 if not left or not top else self.prefix[r1 - 1][c1 - 1]
        return total - left - top + extra

    def make_prefix(self, mat, val):
        m, n = len(mat), len(mat[0])
        self.prefix = [[0] * n for _ in range(m)]
        for row in range(m):
            curr = 0
            for col in range(n):
                curr += mat[row][col] == val
                self.prefix[row][col] = curr + (0 if not row else self.prefix[row - 1][col])

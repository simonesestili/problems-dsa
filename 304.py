class NumMatrix:
    def __init__(self, mat):
        m, n = len(mat), len(mat[0])
        self.prefix = []
        for row in range(m):
            run, curr = [], 0
            for col in range(n):
                curr += mat[row][col]
                run.append((0 if not row else self.prefix[row-1][col]) + curr)
            self.prefix.append(run)

    def sumRegion(self, row1, col1, row2, col2):
        full = self.prefix[row2][col2]
        top = 0 if not row1 else self.prefix[row1-1][col2]
        left = 0 if not col1 else self.prefix[row2][col1-1]
        extra = 0 if not min(row1, col1) else self.prefix[row1-1][col1-1]
        return full - top - left + extra

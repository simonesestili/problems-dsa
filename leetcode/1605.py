class Solution:
    def restoreMatrix(self, rows, cols):
        m, n = len(rows), len(cols)
        mat = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                mat[r][c] = min(rows[r], cols[c])
                rows[r] -= mat[r][c]
                cols[c] -= mat[r][c]

        return mat


class Solution:
    def numSpecial(self, mat):
        m, n = len(mat), len(mat[0])
        rows, cols = [0] * m, [0] * n

        for r in range(m):
            for c in range(n):
                rows[r] += mat[r][c]
                cols[c] += mat[r][c]

        return sum(mat[r][c] and rows[r] == cols[c] == 1 for c in range(n) for r in range(m))

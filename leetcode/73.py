class Solution:
    def setZeroes(self, mat):
        m, n = len(mat), len(mat[0])
        rem_row = any(mat[0][c] == 0 for c in range(n))
        rem_col = any(mat[r][0] == 0 for r in range(m))

        for r in range(1, m):
            for c in range(1, n):
                if mat[r][c] == 0:
                    mat[r][0] = 0
                    mat[0][c] = 0

        for r in range(1, m):
            if mat[r][0] != 0:
                continue
            for c in range(1, n):
                mat[r][c] = 0

        for c in range(1, n):
            if mat[0][c] != 0:
                continue
            for r in range(1, m):
                mat[r][c] = 0

        if rem_row:
            for c in range(n):
                mat[0][c] = 0

        if rem_col:
            for r in range(m):
                mat[r][0] = 0

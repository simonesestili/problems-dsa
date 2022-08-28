class Solution:
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])
        
        def fix(row, col):
            diag, d = [], 0
            while row + d < m and col + d < n:
                diag.append(mat[row + d][col + d])
                d += 1
            diag, d = sorted(diag), 0
            while row + d < m and col + d < n:
                mat[row + d][col + d] = diag[d]
                d += 1

        for r in range(m): fix(r, 0)
        for c in range(1, n): fix(0, c)
        return mat

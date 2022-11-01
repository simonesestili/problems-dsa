class Solution:
    def isToeplitzMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        diags = {}

        for r in range(m):
            for c in range(n):
                if r - c in diags and diags[r - c] != mat[r][c]:
                    return False
                diags[r - c] = mat[r][c]

        return True

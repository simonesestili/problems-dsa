class Solution:
    def rotate(self, mat):
        n = len(mat)

        for c in range(n):
            for r in range(n//2):
                mat[r][c], mat[-r-1][c] = mat[-r-1][c], mat[r][c]

        for r in range(n-1):
            for c in range(r+1, n):
                mat[r][c], mat[c][r] = mat[c][r], mat[r][c]

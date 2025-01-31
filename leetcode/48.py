class Solution:
    def rotate(self, mat):
        n = len(mat)
        for col in range(n):
            for row in range(n // 2):
                mat[row][col], mat[n - 1 - row][col] = mat[n - 1 - row][col], mat[row][col]
        for row in range(n - 1):
            for col in range(row + 1, n):
                mat[row][col], mat[col][row] = mat[col][row], mat[row][col]
        return mat

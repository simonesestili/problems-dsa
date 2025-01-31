class Solution:
    def maximalSquare(self, mat):
        m, n = len(mat), len(mat[0])
        mat = [[int(mat[i][j]) for j in range(n)] for i in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                if mat[row][col]:
                    upleft = mat[row - 1][col - 1]
                    left, up = mat[row][col - 1], mat[row - 1][col]
                    mat[row][col] += min(upleft, left, up)
        return max(map(max, mat)) ** 2

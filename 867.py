class Solution:
    def transpose(self, mat):
        m, n = len(mat), len(mat[0])
        return [[mat[col][row] for col in range(m)] for row in range(n)]

class Solution:
    def transpose(self, mat):
        m, n = len(mat), len(mat[0])
        transposed = [[0] * m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                transposed[row][col] = mat[col][row]
        return transposed

class Solution:
    def sortMatrix(self, mat):
        n = len(mat)
        for r in range(n):
            for i, v in enumerate(sorted((mat[r+i][i] for i in range(n-r)), reverse=True)):
                mat[r+i][i] = v
        for c in range(1, n):
            for i, v in enumerate(sorted(mat[i][c+i] for i in range(n-c))):
                mat[i][c+i] = v
        return mat

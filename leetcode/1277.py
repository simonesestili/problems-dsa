class Solution:
    def countSquares(self, mat):
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i and j and mat[i][j]:
                    mat[i][j] += min(mat[i][j-1], mat[i-1][j], mat[i-1][j-1])
                ans += mat[i][j]
        return ans

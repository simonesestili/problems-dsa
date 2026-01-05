class Solution:
    def maxMatrixSum(self, mat):
        mn = inf
        tot = neg = zero = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                tot += abs(mat[i][j])
                neg += mat[i][j] < 0
                zero += mat[i][j] == 0
                if mat[i][j]:
                    mn = min(mn, abs(mat[i][j]))
        if zero or neg % 2 == 0:
            return tot
        return tot - mn - mn

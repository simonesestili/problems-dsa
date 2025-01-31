class Solution:
    def kthLargestValue(self, mat, k):
        m, n, vals = len(mat), len(mat[0]), []
        for row in range(m):
            curr = 0
            for col in range(n):
                curr ^= mat[row][col]
                mat[row][col] = curr if not row else curr ^ mat[row - 1][col]
                vals.append(mat[row][col])
        return sorted(vals)[-k]

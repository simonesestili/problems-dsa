class Solution:
    def searchMatrix(self, mat, k):
        m, n = len(mat), len(mat[0])
        r, c = 0, n - 1

        while r < m and c >= 0 and mat[r][c] != k:
            c -= mat[r][c] > k
            r += mat[r][c] < k

        return 0 <= r < m and 0 <= c < n

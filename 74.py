class Solution:
    def searchMatrix(self, mat, target):
        m, n = len(mat), len(mat[0])

        lo, hi = 0, m * n - 1
        while lo < hi:
            mid = (lo + hi) >> 1
            val = mat[mid // n][mid % n]
            if val < target: lo = mid + 1
            else: hi = mid

        return mat[lo // n][lo % n] == target

class Solution:
    def maxSideLength(self, mat, mx):
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                prefix[r+1][c+1] = mat[r][c] + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c]

        def valid(k):
            for r in range(m-k+1):
                for c in range(n-k+1):
                    if prefix[r+k][c+k] - prefix[r+k][c] - prefix[r][c+k] + prefix[r][c] <= mx:
                        return True
            return False

        lo, hi = 0, min(m, n)
        while lo < hi:
            k = (lo + hi + 1) // 2
            if valid(k):
                lo = k
            else:
                hi = k - 1
        return lo

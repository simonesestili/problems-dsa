class Solution:
    def rangeAddQueries(self, n, queries):
        mat = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                mat[r][c1] += 1
                if c2 + 1 < n: mat[r][c2+1] -= 1

        for row in range(n):
            for col in range(1, n):
                mat[row][col] += mat[row][col-1]

        return mat

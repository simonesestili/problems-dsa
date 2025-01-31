class Solution:
    def firstCompleteIndex(self, arr, mat):
        m, n = len(mat), len(mat[0])
        vals = {mat[r][c]: (r, c) for c in range(n) for r in range(m)}

        rows, cols = [0] * m, [0] * n
        for i, x in enumerate(arr):
            r, c = vals[arr[i]]
            rows[r] += 1
            cols[c] += 1
            if rows[r] == n or cols[c] == m:
                return i

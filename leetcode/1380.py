class Solution:
    def luckyNumbers(self, mat):
        m, n = len(mat), len(mat[0])
        rows, cols = [min(r) for r in mat], [max([mat[r][c] for r in range(m)]) for c in range(n)]
        return [mat[r][c] for r in range(m) for c in range(n) if mat[r][c] == rows[r] == cols[c]]



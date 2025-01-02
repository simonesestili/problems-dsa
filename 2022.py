class Solution:
    def construct2DArray(self, orig, m, n):
        if len(orig) != m * n: return []
        return [[orig[r*n+c] for c in range(n)] for r in range(m)]


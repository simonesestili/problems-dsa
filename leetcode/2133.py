class Solution:
    def checkValid(self, mat):
        n = len(mat)
        cols = [list() for _ in range(n)]
        for r in mat:
            if len(set(r)) < n: return False
            for i in range(n): cols[i].append(r[i])
        for c in cols:
            if len(set(c)) < n: return False
        return True

class Solution:
    def largestSubmatrix(self, mat):
        m, n = len(mat), len(mat[0])
        rows = [mat[0].copy()]
        for row in mat[1:]:
            rows.append([1 + rows[-1][j] if row[j] else 0 for j in range(n)])

        ans = 0
        for row in rows:
            row.sort(reverse=True)
            for i, h in enumerate(row):
                ans = max(ans, (i + 1) * h)

        return ans

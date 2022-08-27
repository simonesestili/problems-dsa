class Solution:
    def maxSumSubmatrix(self, mat, k):
        m, n = len(mat), len(mat[0])
        prefix = [[0] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                prefix[row].append(prefix[row][-1] + mat[row][col])

        ans = float('-inf')
        for l in range(n):
            for r in range(l, n):
                curr, seen = 0, [0, float('inf')]
                for row in range(m):
                    curr += prefix[row][r+1] - prefix[row][l]
                    extra = bisect_left(seen, curr - k)
                    ans = max(ans, curr - seen[extra])
                    insort(seen, curr)
        return ans


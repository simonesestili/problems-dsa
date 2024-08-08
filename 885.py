DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
class Solution:
    def spiralMatrixIII(self, m, n, r, c):
        ans, i, dirr = [], 0, 0
        while True:
            for _ in range(i // 2 + 1):
                if 0 <= r < m and 0 <= c < n:
                    ans.append([r, c])
                    if len(ans) == m * n:
                        return ans
                dr, dc = DIRS[dirr]
                r, c = r + dr, c + dc
            dirr = (dirr + 1) % 4
            i += 1


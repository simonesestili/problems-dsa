class Solution:
    def findDiagonalOrder(self, mat):
        m, n = len(mat), len(mat[0])
        ans, r, c, d = [], 0, 0, 1
        for _ in range(m*n):
            ans.append(mat[r][c])
            r, c = r-d, c+d
            if c == n:
                r += 2
                c -= 1
                d *= -1
            elif r == -1:
                r += 1
                d *= -1
            elif r == m:
                r -= 1
                c += 2
                d *= -1
            elif c == -1:
                c += 1
                d *= -1
        return ans

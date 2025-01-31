class Solution:
    def findLonelyPixel(self, picture):
        ans, m, n = 0, len(picture), len(picture[0])
        rows, cols = [0] * m, [0] * n

        for row in range(m):
            for col in range(n):
                rows[row] += picture[row][col] == 'B'
                cols[col] += picture[row][col] == 'B'

        for row in range(m):
            for col in range(n):
                ans += picture[row][col] == 'B' and rows[row] == 1 and cols[col] == 1

        return ans

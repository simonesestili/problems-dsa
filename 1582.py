class Solution(object):     
    def numSpecial(self, mat):
        m, n = len(mat), len(mat[0])
        rows, cols = [0] * m, [0] * n
        for row in range(m):
            for col in range(n):
                if mat[row][col]:
                    rows[row] += 1
                    cols[col] += 1

        count = 0
        for row in range(m):
            for col in range(n):
                if rows[row] == 1 and cols[col] == 1 and mat[row][col]:
                    count += 1
        return count

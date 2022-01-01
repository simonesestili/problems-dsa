class Solution:
    def minTotalDistance(self, mat):
        m, n = len(mat), len(mat[0])
        xs = []
        for col in range(n):
            count = 0
            for row in range(m):
                count += mat[row][col]
            for _ in range(count): xs.append(col)
        ys = []
        for row in range(m):
            count = 0
            for col in range(n):
                count += mat[row][col]
            for _ in range(count): ys.append(row)
        dist = 0
        x, y = xs[len(xs) // 2], ys[len(ys) // 2]
        for row in range(m):
            for col in range(n):
                if mat[row][col]:
                    dist += abs(row - y) + abs(col - x)
        return dist


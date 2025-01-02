class Solution:
    def maxPoints(self, points):
        m, n = len(points), len(points[0])

        dp = points[0]
        for i in range(1, m):
            temp = [0] * n
            mx = points[i][0]
            for j in range(1, n):
                mx = max(mx - 1, points[i][j])
                temp[j] = mx
            mx = points[i][-1]
            for j in range(-2, -1, -1):
                mx = max(mx - 1, points[i][j])
                temp[j] = max(temp[j], mx)
            dp = list(a + b for a, b in zip(temp, points[i]))

        return max(dp)

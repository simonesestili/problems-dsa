class Solution:
    def largestTriangleArea(self, points):
        ans = 0
        for i in range(len(points)):
            for j in range(i):
                for k in range(j):
                    xi, xj, xk = points[i][0], points[j][0], points[k][0]
                    yi, yj, yk = points[i][1], points[j][1], points[k][1]
                    ans = max(ans, abs(0.5 * (xi*(yj-yk) + xj*(yk-yi) + xk*(yi-yj))))
        return ans

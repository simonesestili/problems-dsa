class Solution:
    def numberOfPairs(self, points):
        ans, points = 0, sorted(points, key=lambda p: (p[0], -p[1]))
        for i in range(len(points)):
            prev = -1
            for j in range(i + 1, len(points)):
                if prev < points[j][1] <= points[i][1]:
                    prev = points[j][1]
                    ans += 1
        return ans

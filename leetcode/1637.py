class Solution:
    def maxWidthOfVerticalArea(self, points):
        ans, points = 0, sorted(set([x for x, y in points]))
        for i in range(1, len(points)):
            ans = max(ans, points[i] - points[i - 1])
        return ans

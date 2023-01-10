class Solution:
    def maxPoints(self, points):
        lines = defaultdict(set)
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[:i]:
                slope = inf if x1 == x2 else (y2 - y1) / (x2 - x1)
                yint = x1 if slope == inf else y1 - slope * x1
                lines[(slope, yint)].update(((x1, y1), (x2, y2)))
        return max(map(len, lines.values()), default=1)

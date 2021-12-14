class Solution:
    def maxPoints(self, points):
        n, lines = len(points), defaultdict(set)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i):
                x2, y2 = points[j]
                slope = float('inf') if x2 == x1 else (y2 - y1) / (x2 - x1)
                yint = x2 if slope == float('inf') else y1 - slope * x1
                lines[(slope, yint)].add((x1, y1))
                lines[(slope, yint)].add((x2, y2))
        return 1 if n == 1 else max(len(pts) for pts in lines.values())

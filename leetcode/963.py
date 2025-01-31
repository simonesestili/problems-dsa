class Solution:
    def minAreaFreeRect(self, points):
        diags = defaultdict(list)
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i + 1:]:
                xcenter, ycenter = (x1 + x2) / 2, (y1 + y2) / 2
                dist = pow(x2 - x1, 2) + pow(y2 - y1, 2)
                diags[(xcenter, ycenter, dist)].append((x1, y1, x2, y2))

        ans = float('inf')
        for k in diags:
            for i, (x1, y1, x2, y2) in enumerate(diags[k]):
                for x3, y3, x4, y4 in diags[k][:i]:
                    w = sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2))
                    h = sqrt(pow(x1 - x4, 2) + pow(y1 - y4, 2))
                    ans = min(ans, w * h)
        return 0 if ans == float('inf') else ans

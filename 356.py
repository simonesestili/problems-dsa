class Solution:
    def isReflected(self, points):
        points = set([tuple(coord) for coord in points])
        k = (min(points)[0] + max(points)[0]) / 2
        for x, y in points:
            if (2 * k - x, y) not in points: return False
        return True

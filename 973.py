class Solution:
    def kClosest(self, points, k):
        return sorted(points, key=lambda p: sqrt(p[0] ** 2 + p[1] ** 2))[:k]

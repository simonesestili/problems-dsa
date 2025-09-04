class Solution:
    def findClosest(self, x, y, z):
        return 1 if abs(x-z) < abs(y-z) else 2 if abs(y-z) < abs(x-z) else 0

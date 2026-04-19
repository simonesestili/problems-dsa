class Solution:
    def mirrorDistance(self, n):
        return abs(n - int(str(n)[::-1]))

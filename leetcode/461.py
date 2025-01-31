class Solution:
    def hammingDistance(self, x, y):
        a, distance = x ^ y, 0
        while a > 0:
            distance += a & 1
            a >>= 1
        return distance

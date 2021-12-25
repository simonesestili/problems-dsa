class Solution:
    def maximumScore(self, a, b, c):
        a, b, c = sorted([a, b, c])
        return min(a + b, (a + b + c) // 2)

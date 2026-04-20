class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        for i in range(n):
            if colors[0] != colors[-1-i] or colors[i] != colors[-1]:
                return n - 1 - i

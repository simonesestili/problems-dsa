class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        for i in range(n):
            if colors[0] != colors[n - 1 - i] or colors[-1] != colors[i]:
                return n - 1 - i
        return -1

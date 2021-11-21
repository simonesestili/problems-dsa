class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        best = 0
        for i in range(n):
            for j in range(n):
                if colors[i] != colors[j]:
                    best = max(best, abs(j - i))
        return best

class Solution:
    def maxDistance(self, colors):
        ans, n = 0, len(colors)
        for i in range(n):
            if colors[0] != colors[n - 1 - i] or colors[-1] != colors[i]:
                ans = max(ans, n - 1 - i)
        return ans

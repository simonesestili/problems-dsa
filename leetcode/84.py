class Solution:
    def largestRectangleArea(self, heights):
        ans, mono = 0, []
        heights.append(0)
        for i, h in enumerate(heights):
            while mono and heights[mono[-1]] >= h:
                H = heights[mono.pop()]
                W = i if not mono else i - mono[-1] - 1
                ans = max(ans, H * W)
            mono.append(i)
        return ans

class Solution:
    def largestRectangleArea(self, heights):
        mono, ans = [], 0
        heights.append(0)
        for i, height in enumerate(heights):
            while mono and heights[mono[-1]] >= height:
                h = heights[mono.pop()]
                w = i if not mono else i - mono[-1] - 1
                ans = max(ans, h * w)
            mono.append(i)
        return ans

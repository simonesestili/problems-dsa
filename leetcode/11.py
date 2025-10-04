class Solution:
    def maxArea(self, height):
        ans, l, r = 0, 0, len(height) - 1
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]: l += 1
            else: r -= 1
        return ans

class Solution:
    def trap(self, height):
        n, mxright = len(height), height.copy()
        for i in range(n - 2, -1, -1): mxright[i] = max(mxright[i], mxright[i + 1])

        volume = mx = 0
        for i in range(n):
            volume += max(min(mx, mxright[i]) - height[i], 0)
            mx = max(mx, height[i])
        return volume

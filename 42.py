class Solution:
    def trap(self, height):
        n = len(height)
        maxright = [0] * n
        for i in range(n - 2, -1, -1): maxright[i] = max(maxright[i+1], height[i+1])

        volume = maxleft = 0
        
        for i, h in enumerate(height):
            volume += max(min(maxleft, maxright[i]) - h, 0)
            maxleft = max(maxleft, h)

        return volume

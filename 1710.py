class Solution:
    def maximumUnits(self, boxes, size):
        units = [0] * 1001
        for b, u in boxes: units[u] += b
        ans = 0
        for box in range(1000, 0, -1):
            if size == 0: break
            ans += box * min(units[box], size)
            size -= min(units[box], size)
        return ans

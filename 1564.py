class Solution:
    def maxBoxesInWarehouse(self, boxes, warehouse):
        boxes, heights = sorted(boxes, reverse=True), []

        for h in warehouse[::-1]:
            while heights and heights[-1] > h: heights.pop()
            heights.append(h)
        heights = heights[::-1]

        ans = 0
        while boxes and heights:
            while heights and boxes[-1] > heights[-1]: heights.pop()
            if heights:
                ans += 1
                heights.pop()
            boxes.pop()

        return ans

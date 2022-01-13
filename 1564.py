class Solution:
    def maxBoxesInWarehouse(self, boxes, warehouse):
        m, n, boxes = len(boxes), len(warehouse), sorted(boxes, reverse=True)
        for i in range(1, n):
            warehouse[i] = min(warehouse[i], warehouse[i - 1])
        ans = 0
        while boxes and warehouse:
            while warehouse and warehouse[-1] < boxes[-1]: warehouse.pop()
            ans += bool(warehouse)
            if warehouse: boxes.pop(); warehouse.pop();
        return ans


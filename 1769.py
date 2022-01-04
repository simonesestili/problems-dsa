class Solution:
    def minOperations(self, boxes):
        n = len(boxes)
        ans = [0] * n
        curr, count = 0, 0
        for i in range(n):
            ans[i] += curr
            curr += count + (boxes[i] == '1')
            count += boxes[i] == '1'
        curr, count = 0, 0
        for i in range(n - 1, -1, -1):
            ans[i] += curr
            curr += count + (boxes[i] == '1')
            count += boxes[i] == '1'
        return ans


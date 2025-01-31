class Solution:
    def minStartValue(self, nums):
        minimum, curr = float('inf'), 0
        for num in nums:
            curr += num
            minimum = min(minimum, curr)
        return 1 if minimum > 0 else -minimum + 1


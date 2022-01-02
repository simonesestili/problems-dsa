class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, x in enumerate(nums):
            if target - x in seen: return [seen[target - x], i]
            seen[x] = i
        return []

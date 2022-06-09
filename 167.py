class Solution:
    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            curr = nums[left] + nums[right]
            if curr == target: return [left + 1, right + 1]
            elif curr < target: left += 1
            else: right -= 1

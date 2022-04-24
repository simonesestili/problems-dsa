class Solution:
    def intersection(self, nums):
        seen = set(nums[0])
        for i in range(1, len(nums)):
            seen &= set(nums[i])
        return sorted(list(seen))

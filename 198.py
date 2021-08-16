class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        prev, maximum = nums[0], max(nums[0], nums[1])
        for num in nums[2:]:
            prev, maximum = maximum, max(prev + num, maximum)
        return maximum
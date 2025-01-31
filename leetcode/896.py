class Solution:
    def isMonotonic(self, nums):
        inc = dec = 0
        for i in range(len(nums) - 1):
            inc += nums[i+1] >= nums[i]
            dec += nums[i+1] <= nums[i]
        return max(inc, dec) == len(nums) - 1

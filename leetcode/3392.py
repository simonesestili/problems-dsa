class Solution:
    def countSubarrays(self, nums):
        return sum(2 * (nums[i] + nums[i+2]) == nums[i+1] for i in range(len(nums)-2))

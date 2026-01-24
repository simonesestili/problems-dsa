class Solution:
    def minPairSum(self, nums):
        n = len(nums)
        nums.sort()
        return max(nums[i] + nums[n-1-i] for i in range(n//2))

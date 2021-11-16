class Solution:
    def minPairSum(self, nums):
        nums.sort()
        best = float('-inf')
        for i in range(len(nums) // 2):
            best = max(best, nums[i] + nums[len(nums) - 1 - i])
        return best

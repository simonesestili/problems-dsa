class Solution:
    def waysToSplitArray(self, nums):
        ans, prefix, suffix = 0, 0, sum(nums)
        for x in nums[:-1]:
            prefix += x
            suffix -= x
            ans += prefix >= suffix
        return ans

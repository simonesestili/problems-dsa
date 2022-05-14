class Solution:
    def waysToSplitArray(self, nums):
        count, n = 0, len(nums)
        l, r = 0, sum(nums)

        for i in range(n - 1):
            l, r = l + nums[i], r - nums[i]
            count += l >= r

        return count

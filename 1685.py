class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        prefix, suffix = [0] * n, [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i - 1]
            suffix[n - 1 - i] = suffix[n - i] + nums[n - i]
        return [(nums[i] * i - prefix[i]) + (suffix[i] - nums[i] * (n - 1 - i)) for i in range(n)]

class Solution:
    def maximumValueSum(self, nums, k, edges):
        ans = sum(max(x, x ^ k) for x in nums)
        ops = sum(x ^ k > x for x in nums)
        if ops & 1:
            ans -= min(abs(x - (x ^ k)) for x in nums)
        return ans

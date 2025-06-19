class Solution:
    def partitionArray(self, nums, k):
        ans, prev = 0, -inf
        for x in sorted(nums):
            if x - prev > k:
                ans += 1
                prev = x
        return ans

class Solution:
    def longestMonotonicSubarray(self, nums):
        ans = curr = dir = 0
        for i in range(1, len(nums)):
            d = 1 if nums[i] > nums[i-1] else -1 if nums[i] < nums[i-1] else 0
            curr = curr + 1 if d and dir == d else 2 if d else 0
            dir = d
            ans = max(ans, curr)
        return max(ans, 1)

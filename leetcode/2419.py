class Solution:
    def longestSubarray(self, nums):
        ans, curr, mx = 0, 0, max(nums)
        for x in nums:
            if x == mx: curr += 1
            else: curr = 0
            ans = max(ans, curr)
        return ans

class Solution:
    def longestNiceSubarray(self, nums):
        ans = curr = l = 0
        for r in range(len(nums)):
            while nums[r] & curr:
                curr -= nums[l]
                l += 1
            curr |= nums[r]
            ans = max(ans, r - l + 1)
        return ans

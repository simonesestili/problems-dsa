class Solution:
    def countSubarrays(self, nums, k):
        ans, left, mx = 0, 0, max(nums)
        for right, x in enumerate(nums):
            k -= x == mx
            while k + int(nums[left] == mx) <= 0:
                k += nums[left] == mx
                left += 1
            if k <= 0:
                ans += left + 1
        return ans

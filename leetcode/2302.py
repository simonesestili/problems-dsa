class Solution:
    def countSubarrays(self, nums, k):
        ans = left = curr = 0

        for right, x in enumerate(nums):
            curr += x
            while curr * (right - left + 1) >= k:
                curr -= nums[left]
                left += 1
            if curr * (right - left + 1) < k:
                ans += right - left + 1

        return ans

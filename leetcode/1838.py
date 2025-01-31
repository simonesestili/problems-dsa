class Solution:
    def maxFrequency(self, nums, k):
        n, nums = len(nums), sorted(nums)
        ans = left = total = 0
        for right, x in enumerate(nums):
            total += nums[right]
            while (right - left + 1) * x - total > k:
                total -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

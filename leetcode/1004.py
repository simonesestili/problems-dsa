class Solution:
    def longestOnes(self, nums, k):
        n = len(nums)
        ans = left = zeros = 0
        for right in range(n):
            zeros += nums[right] == 0
            while zeros > k:
                zeros -= nums[left] == 0
                left += 1
            ans = max(ans, right - left + 1)

        return ans

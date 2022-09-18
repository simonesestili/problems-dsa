class Solution:
    def smallestSubarrays(self, nums):
        n = len(nums)
        ans, last = [0] * n, [0] * 30
        for i in range(n - 1, -1, -1):
            for j in range(30):
                if nums[i] & 1: last[j] = i
                nums[i] >>= 1
            ans[i] = max(1, max(last) - i + 1)
        return ans

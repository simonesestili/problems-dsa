class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        ans, curr, c = float('inf'), 0, nums.count(1)
        if not c: return 0
        for i in range(c - 1): curr += nums[i]
        left = curr
        for right in range(c - 1, n):
            curr += nums[right]
            ans = min(ans, c - curr)
            curr -= nums[right - c + 1]
        curr = 0
        for i in range(c - 1):
            curr += nums[-1-i]
            ans = min(ans, c - curr - left)
            left -= nums[c - 2 - i]
        return ans

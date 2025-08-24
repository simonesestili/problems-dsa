class Solution:
    def longestSubarray(self, nums):
        ans, curr, use = 0, 0, -1
        for i, x in enumerate(nums):
            if x:
                curr += 1
            else:
                curr = i - use
                use = i
            ans = max(ans, curr)
        return ans - 1

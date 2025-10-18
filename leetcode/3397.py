class Solution:
    def maxDistinctElements(self, nums, k):
        ans, prev = 0, -inf
        for x in sorted(nums):
            use = max(prev + 1, x - k)
            if use <= x + k:
                prev = use
                ans += 1
        return ans

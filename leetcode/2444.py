class Solution:
    def countSubarrays(self, nums, minK, maxK):
        ans, start, mn, mx = 0, -1, -1, -1
        for i, x in enumerate(nums):
            if x == minK: mn = i
            if x == maxK: mx = i
            if x < minK or x > maxK: start = i
            ans += max(min(mn, mx) - start, 0)
        return ans

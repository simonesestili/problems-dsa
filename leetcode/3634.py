class Solution:
    def minRemoval(self, nums, k):
        nums.sort()
        n, r, x = len(nums), 0, 0
        for l in range(n):
            while r + 1 < n and nums[r+1] <= nums[l] * k:
                r += 1
            x = max(x, r - l + 1)
        return n - x

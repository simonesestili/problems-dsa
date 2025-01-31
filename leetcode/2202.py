class Solution:
    def maximumTop(self, nums, k):
        n = len(nums)
        if n == 1: return -1 if k & 1 else nums[0]
        most = float('-inf')
        for i in range(min(k-1,n)): most = max(most, nums[i])
        return max(most, nums[k] if k < n else 0)

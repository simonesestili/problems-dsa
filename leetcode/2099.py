class Solution:
    def maxSubsequence(self, nums, k):
        indices = sorted((x, i) for i, x in enumerate(nums))[-k:]
        indices = set(i for x, i in indices)
        return [x for i, x in enumerate(nums) if i in indices]

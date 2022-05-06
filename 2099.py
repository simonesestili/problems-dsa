class Solution:
    def maxSubsequence(self, nums, k):
        ordered = sorted(((v, i) for i, v in enumerate(nums)), reverse=1)[:k]
        indices = set(i for v, i in ordered)
        return [v for i, v in enumerate(nums) if i in indices]

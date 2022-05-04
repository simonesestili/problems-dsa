class Solution:
    def maxOperations(self, nums, k):
        removed, counts = 0, Counter(nums)
        for num in counts:
            removed += min(counts[num], counts[k - num])
        return removed // 2


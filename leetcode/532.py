class Solution:
    def findPairs(self, nums, k):
        freq = Counter(nums)
        return sum(x - k in freq if k else freq[x - k] > 1 for x in freq)

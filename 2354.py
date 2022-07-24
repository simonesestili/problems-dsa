class Solution:
    def countExcellentPairs(self, nums, k):
        nums, counts = set(nums), defaultdict(int)
        for num in nums: counts[num.bit_count()] += 1
        return sum(sum(counts[i] for i in range(k - num.bit_count(), 30)) for num in nums)

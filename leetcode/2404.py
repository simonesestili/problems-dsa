class Solution:
    def mostFrequentEven(self, nums):
        counts = Counter([x for x in nums if x % 2 == 0])
        mx = max([counts[x] for x in counts])
        for x in sorted(counts.keys()):
            if counts[x] == mx: return x
        return -1

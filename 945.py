class Solution:
    def minIncrementForUnique(self, nums):
        ans, top, counts = 0, -1, Counter(nums)
        for x in sorted(counts.keys()):
            top = max(top, x)
            ans += (top - x) * counts[x] + (counts[x] ** 2 - counts[x]) // 2
            top += counts[x]
        return ans


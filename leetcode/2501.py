class Solution:
    def longestSquareStreak(self, nums):
        ans, seen = -1, defaultdict(int)

        for x in sorted(nums, reverse=True):
            seen[x] = 1 + seen[x*x]
            if seen[x] > 1: ans = max(ans, seen[x])

        return ans

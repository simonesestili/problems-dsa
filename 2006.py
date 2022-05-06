class Solution:
    def countKDifference(self, nums, k):
        ans, seen = 0, defaultdict(int)
        for x in nums:
            ans += seen[x - k] + seen[x + k]
            seen[x] += 1
        return ans


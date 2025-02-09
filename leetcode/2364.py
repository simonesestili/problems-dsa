class Solution:
    def countBadPairs(self, nums):
        ans, seen = len(nums) * (len(nums) - 1) // 2, defaultdict(int)
        for i, x in enumerate(nums):
            ans -= seen[x-i]
            seen[x-i] += 1
        return ans

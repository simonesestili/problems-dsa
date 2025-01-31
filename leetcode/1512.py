class Solution:
    def numIdenticalPairs(self, nums):
        ans, prefix = 0, defaultdict(int)
        for x in nums:
            ans += prefix[x]
            prefix[x] += 1
        return ans

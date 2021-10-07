class Solution:
    def findTargetSumWays(self, nums, target):
        ways = defaultdict(int)
        ways[0] = 1
        for num in nums:
            next_ways = defaultdict(int)
            for curr in ways:
                next_ways[curr - num] += ways[curr]
                next_ways[curr + num] += ways[curr]
            ways = next_ways    
        return ways[target]    


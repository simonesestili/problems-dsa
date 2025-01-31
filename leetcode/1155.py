class Solution:
    def numRollsToTarget(self, d, f, target):
        M = 10 ** 9 + 7

        @lru_cache(None)
        def ways(dice, target):
            if not dice or target < 0:
                return int(not dice and not target)
            count = 0
            for val in range(1, f + 1):
                count = (count + ways(dice - 1, target - val)) % M
            return count
        
        return ways(d, target)

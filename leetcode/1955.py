class Solution:
    def countSpecialSubsequences(self, nums):
        seen, MOD = [0] * 3, pow(10, 9) + 7
        for x in nums:
            if not x: seen[0] += seen[0] + 1
            if x == 1: seen[1] = (seen[1] + seen[1] + seen[0]) % MOD
            if x == 2: seen[2] = (seen[2] + seen[2] + seen[1]) % MOD
        return seen[2]

MOD = 10 ** 9 + 7
class Solution:
    def numOfSubarrays(self, arr):
        ans, curr, seen = 0, 0, {0: 1, 1: 0}
        for x in arr:
            curr = (curr + x) % 2
            ans = (ans + seen[curr ^ 1]) % MOD
            seen[curr] += 1
        return ans

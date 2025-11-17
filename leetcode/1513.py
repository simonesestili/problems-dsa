MOD = 10**9+7
class Solution:
    def numSub(self, s):
        ans = curr = 0
        for x in s:
            if x == '1':
                curr += 1
                ans = (ans + curr) % MOD
            else:
                curr = 0
        return ans

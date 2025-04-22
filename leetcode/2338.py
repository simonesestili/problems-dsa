MOD = 10**9+7
class Solution:
    def idealArrays(self, n, mx):
        ans, prev = mx, [1] * (mx + 1)
        for cnt in range(2, 15):
            curr = [0] * (mx + 1)
            for tail in range(1, mx + 1):
                for mul in range(tail * 2, mx + 1, tail):
                    curr[mul] = (curr[mul] + prev[tail]) % MOD
            ans = (ans + sum(curr) * comb(n - 1, cnt - 1)) % MOD
            prev = curr
        return ans

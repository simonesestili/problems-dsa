MOD = 10**9+7
class Solution:
    def countBalancedPermutations(self, num):
        n, cnts, total = len(num), Counter(map(int, num)), sum(map(int, num))

        @cache
        def dp(d, odd, even, rem):
            if odd == even == rem == 0:
                return 1
            if min(d, odd, even, rem) < 0:
                return 0
            ans = 0
            for cnt in range(0, cnts[d] + 1):
                ans = (ans + comb(odd, cnt) * comb(even, cnts[d] - cnt) * dp(d - 1, odd - cnt, even - cnts[d] + cnt, rem - d * cnt)) % MOD
            return ans

        return 0 if total & 1 else dp(9, n - n//2, n//2, total//2)

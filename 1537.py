class Solution:
    def maxSum(self, a, b):
        MOD = 10 ** 9 + 7
        m, n = len(a), len(b)
        apos, bpos = {x: i for i, x in enumerate(a)}, {x: i for i, x in enumerate(b)}

        @cache
        def dp(i, isa):
            if isa and i >= m or not isa and i >= n: return 0

            res = dp(i + 1, isa) + (a[i] if isa else b[i])
            if isa and a[i] in bpos:
                res = max(res, a[i] + dp(bpos[a[i]] + 1, False))
            elif not isa and b[i] in apos:
                res = max(res, b[i] + dp(apos[b[i]] + 1, True))

            return res

        return max(dp(0, False), dp(0, True)) % MOD

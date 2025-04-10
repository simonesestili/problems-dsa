class Solution:
    def solve(self, mx, limit, s):
        if int(s) > mx: return 0

        mx = str(mx)
        s = s.rjust(len(mx), 'x')

        @cache
        def dp(i, bounded):
            if i >= len(mx): return 1
            if s[i] != 'x': return not bounded or s[i] <= mx[i] and dp(i + 1, s[i] == mx[i])
            return sum(dp(i + 1, bounded and str(d) == mx[i]) for d in range(limit + 1 if not bounded else min(limit, int(mx[i])) + 1))

        return dp(0, True)

    def numberOfPowerfulInt(self, start, finish, limit, s):
        return self.solve(finish, limit, s) - self.solve(start - 1, limit, s)

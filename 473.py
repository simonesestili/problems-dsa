class Solution:
    def makesquare(self, sticks):
        n, sticks = len(sticks), sorted(sticks)
        side, rem = divmod(sum(sticks), 4)
        if n < 4 or rem or sticks[-1] > side: return False

        @cache
        def dp(mask, rem):
            if mask == 0: return rem == 0
            if rem == 0: return dp(mask, side)
            for i in range(n):
                if not mask >> i & 1: continue
                if sticks[i] > rem: break
                if dp(mask - (1 << i), rem - sticks[i]):
                    return True
            return False

        return dp((1 << n) - 1, side)

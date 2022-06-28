class Solution:
    def leastOpsExpressTarget(self, x, target):
        
        @cache
        def dp(val):
            if val < x: return min(2 * val - 1, 2 * (x - val))
            pwr = log2(val) // log2(x)
            best = pwr + dp(val - x ** pwr)
            if x ** (pwr+1) // 2 < val:
                best = min(best, pwr + 1 + dp(x ** (pwr+1) - val))
            return best

        return int(dp(target))

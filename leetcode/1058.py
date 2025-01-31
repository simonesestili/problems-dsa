class Solution:
    def minimizeError(self, prices, target):
        n, prices = len(prices), [int(s.replace('.', '')) for s in prices]

        @cache
        def dp(i, target):
            if i == n: return 0 if not target else float('inf')
            p = prices[i]
            f, c = self.floor(p), self.ceil(p)
            return min(p - f + dp(i + 1, target - f), c - p + dp(i + 1, target - c))

        error = dp(0, target * 1000)
        if error == float('inf'): return '-1'
        error = '0' * max(0, 4 - len(str(error))) + str(error)
        return error[:-3] + '.' + error[-3:]

    def floor(self, n):
        if not n % 1000: return n
        return n - n % 1000

    def ceil(self, n):
        if not n % 1000: return n
        return n + (-n % 1000)

class Solution:
    def maxProfit(self, prices):
        n = len(prices)

        start, mx = [0] * n, prices[-1]
        for i in range(n - 2, -1, -1):
            start[i] = max(mx - prices[i], start[i + 1])
            mx = max(mx, prices[i])

        profit, mn = start[0], prices[0]
        for i in range(1, n - 1):
            profit = max(profit, prices[i] - mn + start[i + 1])
            mn = min(mn, prices[i])

        return profit

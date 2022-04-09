class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        hold, wait = -prices[0] - fee, 0
        for day in range(1, n):
            curr = (max(hold, wait - prices[day] - fee), max(wait, hold + prices[day]))
            hold, wait = curr
        return wait

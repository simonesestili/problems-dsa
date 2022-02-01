class Solution:
	def maxProfit(self, prices):
        profit, buy = 0, float('inf')

        for price in prices:
            profit = max(profit, price - buy)
            buy = min(buy, price)

        return profit

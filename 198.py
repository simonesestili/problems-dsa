class Solution:
    def rob(self, houses):
        prev = profit = 0
        for money in houses:
            prev, profit = profit, max(prev + money, profit)
        return profit

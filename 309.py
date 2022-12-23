class Solution:
    def maxProfit(self, prices):
        holding, waiting, cooling = -inf, 0, 0

        for price in prices:
            holding, waiting, cooling = (
                max(holding, waiting - price),
                max(waiting, cooling),
                holding + price,
            )

        return max(waiting, cooling)

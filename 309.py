class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        # cool[i] is the max profit when cooldowninig at idx i
        # hold[i] is the max profit when holding at idx i
        # sell[i] is the max profit when selling at idx i
        cool, hold, sell = [0] * n, [-prices[0]] * n, [float('-inf')] * n
        for i in range(1, n):
            cool[i] = max(cool[i - 1],  sell[i - 1])
            hold[i] = max(hold[i - 1], cool[i - 1] - prices[i])
            sell[i] = hold[i - 1] + prices[i]
        return max(cool[-1], sell[-1])    

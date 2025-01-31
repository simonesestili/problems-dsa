class Solution:
    def maxProfit(self, prices):
        return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices)))

# class Solution:
#     def maxProfit(self, prices):
#         n = len(prices)
#         ans = 0
#         hold, wait = [0] * n, [0] * n
#         hold[0] = -prices[0]
#         for i in range(1, n):
#             hold[i] = max(hold[i - 1], wait[i - 1] - prices[i])
#             wait[i] = max(wait[i - 1], hold[i - 1] + prices[i])
#             ans = max(ans, wait[i])
#         return ans
# 

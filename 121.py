class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		max_right = [-1] * len(prices)
		curr_max = -1
		for i in range(len(prices) - 1, -1, -1):
			max_right[i] = curr_max
			curr_max = max(curr_max, prices[i])
		
		max_profit = 0
		for i in range(len(prices)):
			max_profit = max(max_profit, max_right[i] - prices[i])
		
		return max_profit

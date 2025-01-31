class Solution:
	def maxScoreSightseeingPair(self, values: List[int]) -> int:
		n = len(values)
		rightside_max = [0] * (n - 1)
		curr_max = -float('inf')
		for j in range(n - 1, 0, -1):
			curr_max = max(curr_max, values[j] - j)
			rightside_max[j - 1] = curr_max
		best_pair = -float('inf')
		for i in range(n - 1):
			best_pair = max(best_pair, values[i] + i + rightside_max[i])
		return best_pair
				

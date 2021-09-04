class Solution:
	def maxIceCream(self, costs: List[int], coins: int) -> int:
		costs.sort()
		count = idx = 0
		
		while idx < len(costs) and costs[idx] <= coins:
			coins -= costs[idx]
			count += 1
			idx += 1		
		
		return count

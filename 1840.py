class Solution:
	def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
		left, right = [9e9] * n, [9e9] * n
		
		# Store restrictions in a dict
		max_heights = {0: 0}
		for idx, max_height in restrictions:
			max_heights[idx - 1] = max_height
		
		# Left
		curr = 0	
		for i in range(n):
			if i in max_heights:
				curr = min(curr, max_heights[i])
			left[i] = curr
			curr += 1

		# Right
		curr = n - 1
		for i in range(n - 1, -1, -1):
			if i in max_heights:
				curr = min(curr, max_heights[i])
			right[i] = curr
			curr += 1	
		
		# Get tallest building
		tallest = 0
		for i in range(n):
			tallest = max(tallest, min(left[i], right[i]))
		
		return tallest	

class Solution:
	def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
		min_row, min_col = m, n
		for row, col in ops:
			min_row, min_col = min(min_row, row), min(min_col, col)
		return min_row * min_col	

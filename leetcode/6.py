class Solution:     
	def convert(self, s: str, numRows: int) -> str: 
		if numRows == 1:
			return s

		levels = [''] * numRows
		level, direction = 0, 1
		for letter in s:
			levels[level] += letter
			if level == 0:
				direction = 1
			elif level == numRows - 1:
				direction = -1
			level += direction
		return ''.join(levels)

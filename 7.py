class Solution:
	def reverse(self, x: int) -> int:
		val, negative = abs(x), x < 0
		val = int(str(val)[::-1])
		if val > pow(2,31) - 1:
			return 0
		return -val if negative else val

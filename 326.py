class Solution:     
	def isPowerOfThree(self, n: int) -> bool: 
		if n <= 0:
			return False
		while n > 1:
			n /= 3
		return n == 1

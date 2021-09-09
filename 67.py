class Solution:
	def addBinary(self, a: str, b: str) -> str:
		if len(a) < len(b):
			a = '0' * (len(b) - len(a)) + a
		elif len(b) < len(a):
			b = '0' * (len(a) - len(b)) + b
		
		bin_sum, n, curr = '', len(a), 0
		
		for i in range(n):
			carry = 1 if curr >= 2 else 0
			curr = int(a[n - 1 - i]) + int(b[n - 1 - i]) + carry
			if curr % 2:
				bin_sum = '1' + bin_sum
			else:
				bin_sum = '0' + bin_sum
		
		return '1' + bin_sum if curr >= 2 else bin_sum
			

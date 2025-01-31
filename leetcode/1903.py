class Solution:
	def largestOddNumber(self, num: str) -> str:
		last = len(num) - 1
		while last >= 0 and int(num[last]) % 2 == 0:
			last -= 1
		return num[:last + 1]

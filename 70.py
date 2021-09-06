class Solution:
	def climbStairs(self, n: int) -> int:
		prev, curr = 1, 1
		for i in range(1,n):
			prev, curr = curr, prev + curr
		return curr	

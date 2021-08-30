class Solution:
	def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
		nums = []
		for i in range(1, 10):
			self.fill(nums, i, n - 1, k) 
		return nums

	def fill(self, nums, num, n, k):
		if n == 0:
			nums.append(num)
			return
		last_digit = num % 10
		if last_digit - k >= 0:
			self.fill(nums, num * 10 + last_digit - k, n - 1, k)
		if last_digit + k <= 9 and k:
			self.fill(nums, num * 10 + last_digit + k, n - 1, k)
		
		

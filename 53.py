class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		max_sum, curr_sum = -9e9, -9e9
		for num in nums:
			curr_sum = max(curr_sum + num, num)
			max_sum = max(max_sum, curr_sum)
		return max_sum

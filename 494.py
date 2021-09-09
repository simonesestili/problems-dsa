class Solution:
	# TLE
	def findTargetSumWays(self, nums: List[int], target: int) -> int:
		return self.sumways(nums, target, 0, 0)

	def sumways(self, nums, target, curr, idx):
		if idx == len(nums):
			return 1 if target == curr else 0
		return (self.sumways(nums, target, curr + nums[idx], idx + 1) +
			self.sumways(nums, target, curr - nums[idx], idx + 1)) 	

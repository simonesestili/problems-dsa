class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		seen = {}
		for idx, num in enumerate(nums):
			other = target - num
			if other in seen:
				return [seen[other], idx]
			seen[num] = idx
					

class Solution:
	def findDuplicates(self, nums: List[int]) -> List[int]:
		duplicates = []
		for num in nums:
			val = abs(num) - 1
			if nums[val] < 0:
				duplicates.append(val + 1)
			nums[val] *= -1
		return duplicates

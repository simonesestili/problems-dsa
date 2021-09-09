class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		subsets = []
		self.get_subsets(nums, [], 0, subsets)
		return subsets
	
	def get_subsets(self, nums, curr, idx, subsets):
		if idx >= len(nums):
			subsets.append(curr.copy())
			return
		self.get_subsets(nums, curr.copy(), idx + 1, subsets)
		curr.append(nums[idx])
		self.get_subsets(nums, curr.copy(), idx + 1, subsets)
		

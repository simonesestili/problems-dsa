class Solution:     
	def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
		return self.construct(nums, 0, len(nums) - 1)
	
	def construct(self, nums, left, right):
		if left > right:
			return None
		max_idx = left
		for i in range(left, right + 1):
			if nums[i] > nums[max_idx]:
				max_idx = i
		return TreeNode(nums[max_idx], self.construct(nums, left, max_idx - 1), self.construct(nums, max_idx + 1, right))
		
			

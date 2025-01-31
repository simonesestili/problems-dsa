class Solution:     
	def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def build(left, right):
            mx = left
            if right < left: return None
            for i in range(left, right + 1):
                if nums[i] > nums[mx]: mx = i
            return TreeNode(nums[mx], left=build(left, mx - 1), right=build(mx + 1, right))
        
        return build(0, len(nums) - 1)

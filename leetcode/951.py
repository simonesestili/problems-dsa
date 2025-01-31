class Solution:
	def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:	
		return self.equal(root1, root2)
	
	def equal(self, root1, root2):
		if not root1 or not root2:
			return root1 == root2
		if root1.val != root2.val:
			return False
		return (self.equal(root1.left, root2.left) and self.equal(root1.right, root2.right) or 
			self.equal(root1.left, root2.right) and self.equal(root1.right, root2.left))	



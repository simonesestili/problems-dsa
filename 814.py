class Solution:
	def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		if root.left:
			self.prune(root.left, root, True)
		if root.right:
			self.prune(root.right, root, False)

		return root if root.left or root.right or root.val else None

	def prune(self, curr, parent, is_left):
		if curr.left:
			self.prune(curr.left, curr, True)
		if curr.right:
			self.prune(curr.right, curr, False)

		if not curr.left and not curr.right and not curr.val:
			if is_left:
				parent.left = None
			else:
				parent.right = None
		


				


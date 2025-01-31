# Second Solution | O(1) insert time
class CBTInserter:
	def __init__(self, root: Optional[TreeNode]):
		self.tree_arr = [root]
		parents = [root]
		children = []
		while parents:
			for parent in parents:
				if parent.left:
					children.append(parent.left)
					self.tree_arr.append(parent.left)
				if parent.right:
					children.append(parent.right)
					self.tree_arr.append(parent.right) 
			parents, children = children, []

	def insert(self, val:int ) -> int:
		count = len(self.tree_arr)
		parent = self.tree_arr[(count - 1) // 2]
		if count % 2:
			parent.left = TreeNode(val)
			self.tree_arr.append(parent.left)
		else:
			parent.right = TreeNode(val)
			self.tree_arr.append(parent.right) 
		return parent.val

	def get_root(self) -> Optional[TreeNode]:
		return self.tree_arr[0]
		


# First Solution | O(n) insert time 
# class CBTInserter:      
#	def __init__(self, root: Optional[TreeNode]):       
#		self.root = root
#	
#
#	def insert(self, val: int) -> int:       
#		if not self.root:
#			self.root = TreeNode(val)
#			return
#		
#		parents = [self.root]
#		children = []
#		while(True):
#			for parent in parents:
#				if not parent.left:
#					parent.left = TreeNode(val)
#					return parent.val
#				if not parent.right:
#					parent.right = TreeNode(val)
#					return parent.val
#				children += [parent.left, parent.right]
#			parents, children = children, []
#	
#	def get_root(self) -> Optional[TreeNode]:
#		return self.root	

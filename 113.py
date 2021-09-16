class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        self.traverse(root, targetSum, 0, [], paths)
        return paths

    def traverse(self, root, targetSum, currSum, path, paths):
        if not root:
            return 

        currSum += root.val
        path.append(root.val)

        if self.isLeaf(root) and targetSum == currSum:
            paths.append(path)

        self.traverse(root.left, targetSum, currSum, path.copy(), paths)
        self.traverse(root.right, targetSum, currSum, path.copy(), paths)

    def isLeaf(self, node):
        return not node.left and not node.right

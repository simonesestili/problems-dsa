class Solution:
    def hasPathSum(self, root, target):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == target
        nextTarget = target - root.val
        return self.hasPathSum(root.left, nextTarget) or self.hasPathSum(root.right, nextTarget)

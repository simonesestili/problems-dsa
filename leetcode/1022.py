class Solution:
    def sumRootToLeaf(self, root):
        self.total = 0

        def dfs(node, prev):
            if not node: return
            curr = (prev << 1) | node.val
            if not node.left and not node.right:
                self.total += curr
            dfs(node.left, curr)
            dfs(node.right, curr)

        dfs(root, 0)
        return self.total

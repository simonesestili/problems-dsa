class Solution:
    def sumNumbers(self, root):
        self.total = 0

        def dfs(node, curr):
            if not node:
                return
            curr = curr * 10 + node.val
            if not node.left and not node.right:
                self.total += curr
                return
            dfs(node.left, curr)
            dfs(node.right, curr)

        dfs(root, 0)
        return self.total

class Solution:
    def goodNodes(self, root):
        self.good = 0

        def dfs(node, maximum):
            if not node:
                return
            self.good += node.val >= maximum
            maximum = max(maximum, node.val)
            dfs(node.left, maximum)
            dfs(node.right, maximum)

        dfs(root, float('-inf'))
        return self.good

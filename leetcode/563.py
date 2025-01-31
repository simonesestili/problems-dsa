class Solution:
    def findTilt(self, root):
        self.tilt = 0

        def dfs(node):
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            self.tilt += abs(left - right)
            return node.val + left + right

        dfs(root)
        return self.tilt

class Solution:
    def distributeCoins(self, root):
        self.ans = 0

        # postorder ans count coins passing through node
        def dfs(node):
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            self.ans += abs(left) + abs(right)
            return node.val - 1 + left + right

        dfs(root)
        return self.ans

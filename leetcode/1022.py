class Solution:
    def sumRootToLeaf(self, root):
        self.ans = 0

        def dfs(node, s=0):
            if not node: return
            s = (s << 1) | node.val
            if not node.left and not node.right:
                self.ans += s
            dfs(node.left, s)
            dfs(node.right, s)

        dfs(root)
        return self.ans

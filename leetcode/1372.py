class Solution:
    def longestZigZag(self, root):
        self.ans = 0
        
        def dfs(node, right, curr):
            if not node: return
            self.ans = max(self.ans, curr)
            if right:
                dfs(node.right, False, curr + 1)
                dfs(node.left, True, 1)
            else:
                dfs(node.left, True, curr + 1)
                dfs(node.right, False, 1)

        dfs(root, False, 0), dfs(root, True, 0)
        return self.ans

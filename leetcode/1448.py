class Solution:
    def goodNodes(self, root):
        dfs = lambda node, mx: 0 if not node else (node.val >= mx) + dfs(node.left, max(mx,node.val)) + dfs(node.right, max(mx,node.val))

        return dfs(root, float('-inf'))

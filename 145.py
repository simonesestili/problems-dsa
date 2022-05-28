class Solution:
    def postorderTraversal(self, root):
        ans = []

        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)

        dfs(root)
        return ans

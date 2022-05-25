class Solution:
    def postorder(self, root):
        ans = []

        def dfs(node):
            if not node: return
            for ch in node.children:
                dfs(ch)
            ans.append(node.val)

        dfs(root)
        return ans

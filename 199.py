class Solution:
    def rightSideView(self, root):
        ans = {}

        def dfs(node, height=0):
            if not node: return
            dfs(node.right, height + 1)
            if height not in ans: ans[height] = node.val
            dfs(node.left, height + 1)

        dfs(root)
        return [ans[i] for i in range(len(ans))]

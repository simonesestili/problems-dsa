class Solution:
    def delNodes(self, root, toDelete):
        ans, toDelete = [], set(toDelete)

        def dfs(node, isroot):
            if node is None: return
            if node.val in toDelete:
                dfs(node.left, True), dfs(node.right, True)
                return
            if isroot: ans.append(node)
            node.left, node.right = dfs(node.left, False), dfs(node.right, False)
            return node

        dfs(root, True)
        return ans


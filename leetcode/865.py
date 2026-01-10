class Solution:
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            if not node:
                return None, 0
            l, ld = dfs(node.left)
            r, rd = dfs(node.right)
            if ld > rd: return l, ld + 1
            if rd > ld: return r, rd + 1
            return node, ld + 1

        return dfs(root)[0]

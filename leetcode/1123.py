class Solution:
    def lcaDeepestLeaves(self, root):
        def dfs(node):
            if node is None:
                return None, 0

            lnode, ldepth = dfs(node.left)
            rnode, rdepth = dfs(node.right)

            if ldepth > rdepth:
                return lnode, 1 + ldepth
            elif ldepth < rdepth:
                return rnode, 1 + rdepth

            return node, 1 + ldepth

        return dfs(root)[0]

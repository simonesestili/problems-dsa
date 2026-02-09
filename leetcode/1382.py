class Solution:
    def balanceBST(self, root):
        vals = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        dfs(root)
        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            return TreeNode(vals[m], build(l, m-1), build(m+1, r))

        return build(0, len(vals)-1)

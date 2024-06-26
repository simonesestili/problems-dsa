class Solution:
    def balanceBST(self, root):
        vals = []

        def dfs(node):
            if node is None: return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        def build(l, r):
            if l > r: return None
            mid = (l + r) // 2
            return TreeNode(vals[mid], build(l, mid - 1), build(mid + 1, r))

        dfs(root)
        return build(0, len(vals) - 1)

class Solution:
    def buildTree(self, inorder, postorder):
        n = len(inorder)
        in_idx = {val: i for i, val in enumerate(inorder)}
        post_idx = {val: i for i, val in enumerate(postorder)}

        def build(in_lo, in_hi, post_lo, post_hi):
            if in_lo == in_hi:
                return TreeNode(inorder[in_lo])
            if in_lo > in_hi:
                return None
            val = postorder[post_hi]
            node = TreeNode(val)
            node.left = build(in_lo, in_idx[val] - 1, post_lo, post_lo + (in_idx[val] - in_lo - 1))
            node.right = build(in_idx[val] + 1, in_hi, post_lo + (in_idx[val] - in_lo), post_hi - 1)
            return node

        return build(0, n - 1, 0, n - 1)

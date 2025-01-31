class Solution:
    def minDiffInBST(self, root):
        def inorder(node):
            if not node: return
            yield from inorder(node.left)
            yield node
            yield from inorder(node.right)

        ans, prev = inf, -inf
        for node in inorder(root):
            ans = min(ans, node.val - prev)
            prev = node.val
        return ans

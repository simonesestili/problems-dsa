class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val > max(p.val, q.val): root = root.left
            elif root.val < min(p.val, q.val): root = root.right
            else: break
        return root

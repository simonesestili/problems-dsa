class Solution:
    def isSameTree(self, p, q):
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) if p and q else p is q

class Solution:
    def sumEvenGrandparent(self, root):
        self.evenSum = 0

        def helper(grandparent, parent, child):
            if not child:
                return
            if grandparent and grandparent.val % 2 == 0:
                self.evenSum += child.val
            helper(parent, child, child.left)
            helper(parent, child, child.right)

        helper(None, None, root)
        return self.evenSum

class Solution:
    def checkEquivalence(self, root1, root2):
        return self.leaves(root1) == self.leaves(root2)

    def leaves(self, root):
        count = [0] * 26
        if root.val != '+':
            count[ord(root.val) - ord('a')] += 1
            return count
        return [a + b for a, b in zip(self.leaves(root.left), self.leaves(root.right))]

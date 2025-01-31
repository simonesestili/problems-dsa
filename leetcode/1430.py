class Solution:
    def isValidSequence(self, root, arr):

        def check(node, i):
            if not node or node.val != arr[i]: return False
            if i == len(arr) - 1: return not node.left and not node.right
            return check(node.left, i + 1) or check(node.right, i + 1)

        return check(root, 0)


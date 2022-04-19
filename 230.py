class Solution:
    def kthSmallest(self, root, k):

        def inorder(node):
            stack = []
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                yield node.val
                node = node.right

        for i, val in enumerate(inorder(root)):
            if i+1 == k:
                return val

        return -1

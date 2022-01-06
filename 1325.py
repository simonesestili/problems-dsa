class Solution:
    def removeLeafNodes(self, root, target):
        dummy = TreeNode(val=target-1, left=root)

        def remove(node):
            if not node: return node
            node.left, node.right = remove(node.left), remove(node.right)
            if not node.left and not node.right and node.val == target: return None
            return node

        return remove(dummy).left

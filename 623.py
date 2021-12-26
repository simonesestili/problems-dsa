class Solution:
    def addOneRow(self, root, val, depth):
        if depth == 1:
            return TreeNode(val=val, left=root)

        curr = [root]
        for _ in range(depth - 2):
            nextt = []
            for node in curr:
                if node.left: nextt.append(node.left)
                if node.right: nextt.append(node.right)
            curr = nextt

        for node in curr:
            node.left = TreeNode(val=val, left=node.left)
            node.right = TreeNode(val=val, right=node.right)
        return root

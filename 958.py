class Solution:
    def isCompleteTree(self, root):
        level = [root]
        while level:
            next_level, missing = [], False
            for node in level:
                if (missing and (node.left or node.right)) or (not node.left and node.right):
                    return False
                if not node.left or not node.right:
                    missing = True
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if missing:
                for node in next_level:
                    if node.left or node.right:
                        return False
                return True
            level = next_level
        return True


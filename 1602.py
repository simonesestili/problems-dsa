class Solution:
    def findNearestRightNode(self, root, u):
        curr = [root]
        while curr:
            next_level = []
            for i, node in enumerate(curr):
                if node is u:
                    return None if i + 1 == len(curr) else curr[i + 1]
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr = next_level
        return None

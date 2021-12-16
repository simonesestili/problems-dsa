class Solution:
    def widthOfBinaryTree(self, root):
        width, level = 0, [(root, 0)]
        while level:
            width = max(width, level[-1][1] - level[0][1] + 1)
            next_level = []
            for node, idx in level:
                if node.left: next_level.append((node.left, idx * 2))
                if node.right: next_level.append((node.right, idx * 2 + 1))
            level = next_level
        return width

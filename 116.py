class Solution:
    def connect(self, root):
        level = [root] if root else []
        while level:
            next_level = []
            for i, node in enumerate(level):
                if i: level[i - 1].next = node
                if not node.left: continue
                next_level.append(node.left)
                next_level.append(node.right)
            level = next_level
        return root

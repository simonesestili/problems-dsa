class Solution:
    def levelOrderBottom(self, root):
        ans, level = [], [root] if root else []
        while level:
            ans.append([node.val for node in level])
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        return reversed(ans)

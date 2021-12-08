class Solution:
    def zigzagLevelOrder(self, root):
        ans, level, right = [], [root] if root else [], True
        while level:
            next_level = []
            ans.append([node.val for node in (level if right else level[::-1])])
            right = not right
            for node in level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            level = next_level
        return ans

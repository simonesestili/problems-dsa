class Solution:
    def rightSideView(self, root):
        ans = []
        level = [root] if root else []
        while level:
            ans.append(level[-1].val)
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level

        return ans

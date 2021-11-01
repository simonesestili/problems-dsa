class Solution:
    def levelOrder(self, root):
        ans = []
        level = [root] if root else []
        while level:
            next_level = []
            vals = []
            for node in level:
                vals.append(node.val)
                for child in node.children:
                    next_level.append(child)
            ans.append(vals)
            level = next_level
        return ans

class Solution:
    def averageOfLevels(self, root):
        ans, level = [], [root]
        while level:
            nxt, total, count = [], 0, 0
            for node in level:
                total, count = total + node.val, count + 1
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            ans.append(total / count)
            level = nxt
        return ans

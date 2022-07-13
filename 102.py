class Solution:
    def levelOrder(self, root):
        ans, level = [], [root] if root else []

        while level:
            ans.append([])
            nxtlvl = []
            for node in level:
                if node.left: nxtlvl.append(node.left)
                if node.right: nxtlvl.append(node.right)
                ans[-1].append(node.val)
            level = nxtlvl

        return ans

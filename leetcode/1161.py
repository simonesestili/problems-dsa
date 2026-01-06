class Solution:
    def maxLevelSum(self, root):
        ans, mx, curr, i = 1, -inf, [root], 0
        while curr:
            s, nxt, i = 0, [], i + 1
            for node in curr:
                s += node.val
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            if s > mx:
                ans, mx = i, s
            curr = nxt
        return ans

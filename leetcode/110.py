class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if not node:
                return 0, True
            ld, l = dfs(node.left)
            rd, r = dfs(node.right)
            return 1 + max(ld, rd), abs(ld - rd) <= 1 and l and r

        return dfs(root)[1]


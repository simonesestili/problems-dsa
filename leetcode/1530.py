class Solution:
    def countPairs(self, root, d):
        self.ans = 0

        def dfs(node):
            if not node: return []
            if not node.left and not node.right: return [1]
            l, r = dfs(node.left), dfs(node.right)
            self.ans += sum(x + y <= d for x in l for y in r)
            return [x+1 for x in l+r if x+1 <= d]

        dfs(root)
        return self.ans


MOD = 10 ** 9 + 7
class Solution:
    def maxProduct(self, root):
        total = 0
        self.min_diff = float('inf')

        def dfs(node):
            if not node: return 0
            ans = node.val + dfs(node.left) + dfs(node.right)
            if total and abs(total - ans - ans) < self.min_diff:
                self.min_diff = abs(total - ans - ans)
            return ans

        total = dfs(root)
        dfs(root)

        a = (total - self.min_diff) // 2
        b = total - a
        return a * b % MOD

class Solution:
    def solve(self, root):
        self.count = 0

        def dfs(node):
            if not node: return True
            left, right = dfs(node.left), dfs(node.right)
            if not left or not right: return False
            ans = ((not node.left or node.left.val == node.val) and 
                    (not node.right or node.right.val == node.val))
            self.count += ans
            return ans

        dfs(root)
        return self.count

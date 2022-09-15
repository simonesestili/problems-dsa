class Solution:
    def pseudoPalindromicPaths(self, root):
        self.ans, counts = 0, defaultdict(int)
        isleaf = lambda x: x.left is None and x.right is None

        def dfs(node=root, odds=0):
            if node is None: return
            counts[node.val] += 1
            odds += 1 if counts[node.val] & 1 else -1
            if isleaf(node): self.ans += odds <= 1
            dfs(node.left, odds)
            dfs(node.right, odds)
            counts[node.val] -= 1

        dfs()
        return self.ans

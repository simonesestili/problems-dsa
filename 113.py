class Solution:
    def pathSum(self, root, target):
        ans, curr = [], []
        isleaf = lambda x: x.left is None and x.right is None

        def dfs(node, k):
            if node is None: return
            curr.append(node.val)
            k -= node.val
            if isleaf(node) and k == 0: ans.append(curr.copy())
            dfs(node.left, k)
            dfs(node.right, k)
            curr.pop()

        dfs(root, target)
        return ans

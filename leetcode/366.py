class Solution:
    def findLeaves(self, root):
        depths = defaultdict(list)

        def dfs(node):
            if not node: return 0
            depth = 1 + max(dfs(node.left), dfs(node.right))
            depths[depth].append(node.val)
            return depth

        dfs(root)
        return [depths[d+1] for d in range(len(depths))]

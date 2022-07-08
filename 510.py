class Solution:
    def inorderSuccessor(self, target):
        root = target
        while root.parent: root = root.parent

        def dfs(node):
            if node:
                yield from dfs(node.left)
                yield node
                yield from dfs(node.right)

        prev = None
        for curr in dfs(root):
            if prev is target:
                return curr
            prev = curr
        return None

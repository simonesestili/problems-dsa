class Solution:
    def isSubPath(self, head, root):
        if not head: return True
        if not root: return False

        def dfs(node, tree):
            if not node: return True
            if not tree: return False
            return node.val == tree.val and (dfs(node.next, tree.left) or dfs(node.next, tree.right))

        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

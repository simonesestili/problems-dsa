class Solution:
    def cloneTree(self, root):

        def clone(node):
            if not node: return None
            copy = Node(node.val)
            for child in node.children:
                copy.children.append(clone(child))
            return copy

        return clone(root)

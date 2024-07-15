class Solution:
    def createBinaryTree(self, desc):
        nodes, roots = {}, set((p for p, c, l in desc))
        for p, c, l in desc:
            roots.discard(c)
            if p not in nodes: nodes[p] = TreeNode(val=p)
            if c not in nodes: nodes[c] = TreeNode(val=c)
            if l: nodes[p].left = nodes[c]
            else: nodes[p].right = nodes[c]
        return nodes[roots.pop()]


class Solution:
    def createBinaryTree(self, desc):
        nodes, children, parents = {}, set(), set()
        for parent, child, left in desc:
            if parent not in nodes: nodes[parent] = TreeNode(parent)
            if child not in nodes: nodes[child] = TreeNode(child)

            if left: nodes[parent].left = nodes[child]
            else: nodes[parent].right = nodes[child]

            parents.add(parent)
            children.add(child)

        root = (parents - children).pop()
        return nodes[root]


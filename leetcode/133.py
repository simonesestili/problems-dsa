class Solution:
    def cloneGraph(self, main):
        if not main: return None
        nodes = [None] * 101

        def clone(node):
            if nodes[node.val]:
                return nodes[node.val]
            nodes[node.val] = Node(node.val)
            for neigh in node.neighbors:
                nodes[node.val].neighbors.append(clone(neigh))
            return nodes[node.val]

        return clone(main)

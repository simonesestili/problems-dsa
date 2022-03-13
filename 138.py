class Solution:
    def copyRandomList(self, head):
        nodes = {}

        def copy(node):
            if not node: return None
            if node in nodes: return nodes[node]
            copied = nodes[node] = Node(node.val)
            copied.next, copied.random = copy(node.next), copy(node.random)
            return nodes[node]

        return copy(head)

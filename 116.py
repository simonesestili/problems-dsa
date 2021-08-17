"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        curr = [root]
        while curr:
            next_layer = []
            # Settings nexts
            for i in range(len(curr)):
                if curr[i].left:
                    next_layer.append(curr[i].left)
                    next_layer.append(curr[i].right)
                if i == len(curr) - 1:
                    curr[i].next = None
                else:
                    curr[i].next = curr[i + 1]
            curr = next_layer
        return root
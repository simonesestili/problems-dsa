class Solution:
    def swapPairs(self, head):
        
        def swap(node):
            if not node or not node.next: return node
            nextt = node.next
            node.next = swap(nextt.next)
            nextt.next = node
            return nextt

        return swap(head)

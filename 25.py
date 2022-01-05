class Solution:
    def reverseKGroup(self, head, k):

        def group(node):
            curr = prev = node
            for _ in range(k):
                if not curr: return node
                prev, curr = curr, curr.next
            prev.next = None
            head = self.reverse(node)
            node.next = group(curr)
            return head

        return group(head)

    def reverse(self, node):
        prev, curr, nextt = None, node, None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev, curr = curr, nextt
        return prev

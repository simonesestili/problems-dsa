class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return self.swap(head)

    def swap(self, node):
        if not node or not node.next:
            return node
        first, second, third = node, node.next, node.next.next
        first.next = self.swap(third)
        second.next = first
        return second

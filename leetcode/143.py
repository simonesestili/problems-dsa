class Solution:
    def reorderList(self, head):
        if not head.next: return head
        slow = fast = prev = head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None
        curr, alt = head, self.reverse(slow)
        while alt:
            temp = curr.next
            curr.next = alt
            curr = alt
            alt = temp

    def reverse(self, node):
        prev, curr, nextt = None, node, None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        return prev

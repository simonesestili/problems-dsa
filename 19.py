class Solution:
    def removeNthFromEnd(self, head, n):
        slow = fast = head
        for _ in range(n): fast = fast.next
        while fast: slow, fast = slow.next, fast.next
        slow.next = None if slow.next is None else slow.next.next
        return dummy.next

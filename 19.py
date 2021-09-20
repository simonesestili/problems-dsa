class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        for i in range(n + 1):
            if not fast:
                return head.next
            fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next
        slow.next = None if not slow.next else slow.next.next    
        return head

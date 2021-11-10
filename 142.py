class Solution:
    def detectCycle(self, head):
        seen = set()
        idx = 0
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
            idx += 1
        return -1

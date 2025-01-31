class Solution:
    def oddEvenList(self, head):
        if not head: return head
        odds = curr_odd = ListNode(val=-1)
        prev, curr, idx = None, head, 0
        while curr:
            if idx % 2:
                next, curr.next = curr.next, None
                curr_odd.next = curr
                curr_odd = curr_odd.next
                prev.next = next
                curr = next
            else:
                prev, curr = curr, curr.next
            idx += 1
        tail = head
        while tail.next:
            tail = tail.next
        tail.next = odds.next
        return head

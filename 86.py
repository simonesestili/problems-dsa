class Solution:
    def partition(self, head, x):
        left_head = left_tail = ListNode()
        right_head = right_tail = ListNode()

        while head:
            if head.val < x:
                left_tail.next = head
                left_tail = left_tail.next
            else:
                right_tail.next = head
                right_tail = right_tail.next
            prev = head
            head, prev.next = prev.next, None

        left_tail.next = right_head.next
        return left_head.next

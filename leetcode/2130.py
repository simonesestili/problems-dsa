class Solution:
    def pairSum(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        head2, slow.next = slow.next, None
        head2 = self.reverse(head2)
        best = 0
        while head and head2:
            best = max(best, head.val + head2.val)
            head, head2 = head.next, head2.next
        return best

    def reverse(self, head):
        prev, curr, nextt = None, head, None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev, curr = curr, nextt
        return prev

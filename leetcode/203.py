class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(val=val - 1, next=head)
        curr = dummy
        while curr and curr.next:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return dummy.next

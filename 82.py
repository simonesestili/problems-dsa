class Solution:
    def deleteDuplicates(self, head):
        curr = dummy = ListNode(val=float('inf'), next=head)
        while curr:
            flag = False
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                flag, val = True, curr.next.val
                while curr.next and curr.next.val == val:
                    curr.next = curr.next.next
            curr = curr if flag else curr.next
        return dummy.next

class Solution:
    def insertionSortList(self, head):
        ans = ListNode(float('-inf'))
        while head:
            curr = ans
            while curr.next and curr.next.val < head.val: # find insertion point
                curr = curr.next
            curr.next = ListNode(val=head.val, next=curr.next) # insert node
            head = head.next # consume input node inserted
        return ans.next

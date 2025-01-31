class Solution:
    def deleteDuplicates(self, head):
        dummy = curr = ListNode(float('inf'), head)

        while curr.next:
            val = curr.next.val
            if not curr.next.next or val != curr.next.next.val:
                curr = curr.next
                continue
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next

        return dummy.next


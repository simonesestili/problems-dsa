class Solution: 
    def mergeTwoLists(self, a, b):
        dummy = curr = ListNode()

        while a and b:
            if a.val < b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next

        if a: curr.next = a
        if b: curr.next = b
        return dummy.next

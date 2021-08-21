# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            if not l1:
                return l2
            else:
                return l1
            
        
        if l1.val < l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            l2 = l2.next
        
        curr = head
        
        while l1 or l2:
            if not l1:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            elif not l2:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    curr.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    curr.next = ListNode(l2.val)
                    l2 = l2.next
            curr = curr.next
        
        return head
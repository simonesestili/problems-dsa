# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        placeholder = ListNode(val = -1, next = head)
        curr = placeholder
        
        while curr:
            if curr.next and curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return placeholder.next
        
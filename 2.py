# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        summed = 0
        while l1 or l2:
            if l1:
                summed += l1.val
                l1 = l1.next
            if l2:
                summed += l2.val
                l2 = l2.next
            curr.next = ListNode(val=summed % 10)
            summed //= 10
            curr = curr.next
        if summed:
            curr.next = ListNode(val=summed)
        return res.next
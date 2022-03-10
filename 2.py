class Solution:
    def addTwoNumbers(self, l1, l2):
        ans = curr = ListNode()
        carry = 0
        while l1 or l2:
            v1, v2 = 0 if not l1 else l1.val, 0 if not l2 else l2.val
            carry, val = divmod(carry + v1 + v2, 10)
            curr.next = ListNode(val)
            curr = curr.next
            l1, l2 = l1 if not l1 else l1.next, l2 if not l2 else l2.next

        if carry: curr.next = ListNode(carry)
        return ans.next


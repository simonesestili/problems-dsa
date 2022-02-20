class Solution:
    def mergeNodes(self, head):
        ans = []
        curr = 0
        head = head.next
        while head:
            if head.val == 0:
                ans.append(curr)
                curr = 0
            else:
                curr += head.val
            head = head.next
        dummy = curr = ListNode()
        for x in ans:
            curr.next = ListNode(val=x)
            curr = curr.next
        return dummy.next


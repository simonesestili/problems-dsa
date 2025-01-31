class Solution:
    def deleteMiddle(self, head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.pop(len(arr) // 2)
        dummy = ListNode(-1)
        curr = dummy
        for x in arr:
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next


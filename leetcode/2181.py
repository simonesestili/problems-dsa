class Solution:
    def mergeNodes(self, head):
        curr = 0
        slow = fast = head
        while fast.next:
            fast = fast.next
            curr += fast.val
            if not fast.val:
                slow.val = curr
                if fast.next is None: slow.next = None
                slow = slow.next
                curr = 0
        return head


class Solution:
    def swapNodes(self, head, k):
        slow = fast = head
        for _ in range(k): fast = fast.next

        while fast:
            slow, fast = slow.next, fast.next

        left, right = head, slow
        for _ in range(k - 1): left = left.next

        left.val, right.val = right.val, left.val
        return head

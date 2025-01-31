class Solution:
    def rotateRight(self, head, k):
        if not k or not head: return head

        tail, curr, length = None, head, 0
        while curr: tail, curr, length = curr, curr.next, length + 1
        k = -k % length

        if not k: return head

        prev, curr = None, head
        for _ in range(k): prev, curr = curr, curr.next
        tail.next, prev.next = head, None

        return curr

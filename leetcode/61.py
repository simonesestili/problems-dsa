class Solution:
    def rotateRight(self, head, k):
        curr, tail, n = head, head, 0
        while curr:
            n += 1
            tail = curr
            curr = curr.next

        if not n or not k%n:
            return head

        k %= n
        curr = head
        for _ in range(n-k-1):
            curr = curr.next

        tail.next, head, curr.next = head, curr.next, None
        return head

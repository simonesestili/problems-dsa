class Solution:
    def splitListToParts(self, head, k):
        n, parts = self.length(head), []
        size, extra = divmod(n, k)

        for i in range(k):
            temp = head
            for j in range(size + (i < extra) - 1):
                if not head: break
                head = head.next
            if head: head, head.next = head.next, None
            parts.append(temp)

        return parts

    def length(self, head, n=0):
        while head:
            n, head = n + 1, head.next
        return n

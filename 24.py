class Solution:
    def swapPairs(self, head):
        if not head or not head.next: return head
        nextt = head.next
        head.next = self.swapPairs(nextt.next)
        nextt.next = head
        return nextt

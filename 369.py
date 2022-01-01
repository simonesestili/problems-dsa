class Solution:
    def plusOne(self, head):
        head = curr = self.reverse(head)
        prev, inc = None, True
        while curr:
            curr.val += 1
            if curr.val != 10:
                inc = False
                break
            curr.val = 0
            prev, curr = curr, curr.next
        if inc: prev.next = ListNode(1)
        return self.reverse(head)

    def reverse(self, head):
        prev, curr, nextt = None, head, None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev, curr = curr, nextt
        return prev

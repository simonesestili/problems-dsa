class Solution:
    def getDecimalValue(self, head):
        ans = 0
        while head:
            ans <<= 1
            ans += head.val
            head = head.next
        return ans

class Solution:
    def getIntersectionNode(self, headA, headB):

        def length(node, res=0):
            while node: node, res = node.next, res + 1
            return res
        
        if length(headA) < length(headB): headA, headB = headB, headA
        for _ in range(length(headA) - length(headB)): headA = headA.next

        while headA is not headB:
            headA, headB = headA.next, headB.next

        return headA

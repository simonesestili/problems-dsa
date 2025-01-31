class Solution:
    def removeKdigits(self, num, k):
        stack = []

        for d in num:
            while stack and stack[-1] > d and k:
                stack.pop()
                k -= 1
            stack.append(d)

        while k and stack:
            stack.pop()
            k -= 1

        return '0' if not stack else str(int(''.join(stack)))

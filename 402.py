class Solution:
    def removeKdigits(self, num, k):
        stack, i = [], 0

        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        while i < len(stack) and stack[i] == '0': i += 1
        stack = stack[i:]

        while k and stack:
            stack.pop()
            k -= 1

        return '0' if not stack else ''.join(stack)

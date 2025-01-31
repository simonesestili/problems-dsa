class Solution:
    def decodeString(self, s):
        stack, curr, num = [], '', 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append((curr, num))
                curr, num = '', 0
            elif c == ']':
                prev, k = stack.pop()
                curr = prev + curr * k
            else:
                curr += c
        return curr

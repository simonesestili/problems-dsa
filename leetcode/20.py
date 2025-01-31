class Solution:
    def isValid(self, s):
        stack, pairs = [], {')': '(', '}': '{', ']': '['}
        for c in s:
            if c not in pairs:
                stack.append(c)
            elif stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                return False
        return len(stack) == 0

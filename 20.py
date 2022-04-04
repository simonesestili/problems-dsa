class Solution:
    def isValid(self, s):
        stack, pairs = [], {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in pairs:
                if not stack or pairs[c] != stack.pop():
                    return False
            else:
                stack.append(c)

        return len(stack) == 0


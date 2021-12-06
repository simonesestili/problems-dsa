class Solution:
    def isValid(self, s):
        stack = []
        for c in s:
            if c == 'c':
                if not stack or stack.pop() != 'b': return False
                if not stack or stack.pop() != 'a': return False
            else:
                stack.append(c)
        return not stack

class Solution:
    def isValid(self, s):
        stack, matches = [], {')':'(', '}':'{', ']':'['}

        for c in s:
            if c not in matches: stack.append(c)
            elif not stack: return False
            elif stack.pop() != matches[c]: return False

        return not stack

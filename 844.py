class Solution:
    def backspaceCompare(self, s, t):
        
        def extract(code):
            stack = []
            for c in code:
                if c == '#' and stack: stack.pop()
                elif c != '#': stack.append(c)
            return ''.join(stack)

        return extract(s) == extract(t)

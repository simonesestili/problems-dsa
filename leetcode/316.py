class Solution:
    def removeDuplicateLetters(self, s):
        last = [-1] * 26
        code = lambda c: ord(c) - ord('a')
        for i, c in enumerate(s): last[code(c)] = i
        
        stack, added = ['A'], 0
        for i, c in enumerate(s):
            if added >> code(c) & 1: continue
            while c < stack[-1] and last[code(stack[-1])] > i:
                added -= 1 << code(stack.pop())
            added |= 1 << code(c)
            stack.append(c)

        return ''.join(stack[1:])

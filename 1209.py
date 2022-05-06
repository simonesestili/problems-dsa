class Solution:
    def removeDuplicates(self, s, k):
        stack = [['!', 0]]
        for c in s:
            prev, cnt = stack[-1]
            if c == prev: stack[-1][1] += 1
            else: stack.append([c, 1])
            if stack[-1][1] == k: stack.pop()

        return ''.join(c * cnt for c, cnt in stack[1:])
                

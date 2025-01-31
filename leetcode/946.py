class Solution:   
	def validateStackSequences(self, pushed, popped):
        stack = []
        n, i, j = len(pushed), 0, 0

        while i < n or j < n:
            if stack and j < n and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            elif i < n:
                stack.append(pushed[i])
                i += 1
            else: return False

        return not stack

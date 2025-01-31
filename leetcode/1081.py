class Solution:
    def smallestSubsequence(self, s):
        stack, last = [], {c: i for i, c in enumerate(s)}
        used = set()

        for i, c in enumerate(s):
            if c in used: continue
            while stack and c < stack[-1] and last[stack[-1]] > i:
                used.remove(stack.pop())
            stack.append(c)
            used.add(c)

        return ''.join(stack)

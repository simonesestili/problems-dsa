class Solution:
    def smallestNumber(self, pattern):
        ans, stack = [], []
        for i, c in enumerate(pattern + 'I'):
            stack.append(str(i + 1))
            while c == 'I' and stack:
                ans.append(stack.pop())
        return ''.join(ans)

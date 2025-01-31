class Solution:
    def minAddToMakeValid(self, s):
        left = right = 0
        for c in s:
            if c == '(':
                right += 1
            elif c == ')':
                if not right:
                    left += 1
                else:
                    right -= 1
        return left + right
class Solution:
    def reverseParentheses(self, s):
        ans = ['']
        for c in s:
            if c == '(':
                ans.append('')
            elif c == ')':
                ans[len(ans) - 2] += ans.pop()[::-1]
            else:
                ans[-1] += c
        return ''.join(ans)


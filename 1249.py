class Solution:
    def minRemoveToMakeValid(self, s):
        ans, count, rem = [], 0, s.count(')')

        for c in s:
            if c == ')':
                rem -= 1
                if not count: continue
                count -= 1
                ans.append(c)
            elif c == '(':
                if rem < count + 1: continue
                count += 1
                ans.append(c)
            else:
                ans.append(c)

        return ''.join(ans)

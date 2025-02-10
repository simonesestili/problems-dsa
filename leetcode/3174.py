class Solution:
    def clearDigits(self, s):
        ans = []
        for c in s:
            if not c.isdigit():
                ans.append(c)
            elif ans:
                ans.pop()
        return ''.join(ans)

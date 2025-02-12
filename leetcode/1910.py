class Solution:
    def removeOccurrences(self, s, part):
        ans, m = [], len(part)
        for c in s:
            ans.append(c)
            if ''.join(ans[-m:]) == part:
                ans = ans[:-m]
        return ''.join(ans)

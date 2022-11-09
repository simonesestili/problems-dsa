class Solution:
    def makeGood(self, s):
        ans = []
        opp = lambda c: c.upper() if c.islower() else c.lower()
        for c in s:
            if ans and opp(ans[-1]) == c: ans.pop()
            else: ans.append(c)
        return ''.join(ans)

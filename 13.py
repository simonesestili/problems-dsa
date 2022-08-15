V = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
class Solution:
    def romanToInt(self, s):
        ans = mx = 0
        for c in reversed(s):
            if V[c] < mx: ans -= V[c]
            else: ans += V[c]
            mx = max(mx, V[c])
        return ans

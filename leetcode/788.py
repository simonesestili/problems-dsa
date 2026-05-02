INVALID = {'3', '4', '7'}
CHANGE = {'2', '5', '6', '9'}
class Solution:
    def rotatedDigits(self, n):
        ans = 0
        for x in range(1, n+1):
            change = 0
            for d in str(x):
                if d in INVALID: break
                change += d in CHANGE
            else:
                ans += bool(change)
        return ans

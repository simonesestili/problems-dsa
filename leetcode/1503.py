class Solution:
    def getLastMoment(self, n, left, right):
        ans = 0
        for x in left: ans = max(ans, x)
        for x in right: ans = max(ans, n - x)
        return ans

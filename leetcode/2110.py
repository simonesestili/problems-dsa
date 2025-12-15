class Solution:
    def getDescentPeriods(self, prices):
        ans = curr = 0
        for i in range(len(prices)):
            if i and prices[i - 1] != prices[i] + 1:
                curr = 0
            curr += 1
            ans += curr
        return ans

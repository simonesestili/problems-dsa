class Solution:
    def getDescentPeriods(self, prices):
        n, diffs = len(prices), []
        for i in range(1, n):
            diffs.append(prices[i - 1] - prices[i])
        diffs.append(0)
        ans = n
        curr = 0
        for diff in diffs:
            if diff == 1:
                curr += 1
            else:
                ans += self.gauss(curr)
                curr = 0
        return ans

    def gauss(self, n):
        return n * (n + 1) // 2



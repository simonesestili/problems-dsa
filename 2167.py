#Q4
class Solution:
    def minimumTime(self, s):
        left = self.costs(s)
        right = self.costs(s[::-1])

        ans = min(right[-1], left[-1])
        for i in range(len(s) - 1):
            ans = min(ans, left[i] + right[-1-i])
        return ans

    def costs(self, s):
        costs = [0] * len(s)
        for i, x in enumerate(s):
            prev = 0 if not i else costs[i - 1]
            costs[i] = prev if x == '0' else min(i + 1, prev + 2)
        return costs

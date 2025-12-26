class Solution:
    def maximumHappinessSum(self, happiness, k):
        return sum(max(x - i, 0) for i, x in enumerate(nlargest(k, happiness)))

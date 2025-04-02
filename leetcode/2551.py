class Solution:
    def putMarbles(self, weights, k):
        cuts = sorted([weights[i] + weights[i + 1] for i in range(len(weights) - 1)])
        return sum(nlargest(k - 1, cuts)) - sum(nsmallest(k - 1, cuts))

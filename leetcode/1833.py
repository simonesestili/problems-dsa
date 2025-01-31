class Solution:
    def maxIceCream(self, costs, coins):
        for bars, cost in enumerate(sorted(costs)):
            if cost > coins: return bars
            coins -= cost
        return len(costs)

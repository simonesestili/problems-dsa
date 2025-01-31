class Solution:
    def minimumCost(self, cost):
        total, cost = sum(cost), sorted(cost, reverse=True)
        for i in range(len(cost) // 3):
            total -= cost[2 + i * 3]
        return total

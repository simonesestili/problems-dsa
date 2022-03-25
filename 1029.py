class Solution:
    def twoCitySchedCost(self, costs):
        n, costs = len(costs), sorted(costs, key=lambda x: -abs(x[0] - x[1]))
        cost = a = b = 0

        for acost, bcost in costs:
            if a == n >> 1: cost, b = cost + bcost, b + 1
            elif b == n >> 1: cost, a = cost + acost, a + 1
            elif acost < bcost: cost, a = cost + acost, a + 1
            else: cost, b = cost + bcost, b + 1

        return cost

class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas): return -1

        n, curr, idx = len(cost), 0, 0
        for i in range(n):
            curr += gas[i] - cost[i]
            if curr < 0: curr, idx = 0, i + 1

        return idx

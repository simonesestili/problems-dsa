class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas): return -1

        curr = station = 0
        for i, gain in enumerate((g - c for g, c in zip(gas, cost))):
            curr += gain
            if curr < 0:
                curr, station = 0, i + 1

        return station

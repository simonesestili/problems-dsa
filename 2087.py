class Solution:
    def minCost(self, curr, home, rows, cols):
        cost = 0
        while curr != home:
            if curr[0] != home[0]:
                curr[0] += 1 if curr[0] < home[0] else -1
                cost += rows[curr[0]]
            if curr[1] != home[1]:
                curr[1] += 1 if curr[1] < home[1] else -1
                cost += cols[curr[1]]
        return cost

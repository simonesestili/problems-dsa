class Solution:
    def minSideJumps(self, obstacles):
        costs = [1, 0, 1]

        for o in obstacles[1:]:
            nextt = [costs[i] if i + 1 != o else float('inf') for i in range(3)]
            best = min(nextt)
            for i in range(3):
                if o != i + 1:
                    nextt[i] = min(nextt[i], best + 1)
            costs = nextt

        return min(costs)

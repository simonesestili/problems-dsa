class Solution:
    def connectSticks(self, sticks):
        cost = 0
        heapify(sticks)
        while len(sticks) > 1:
            x, y = heappop(sticks), heappop(sticks)
            heappush(sticks, x + y)
            cost += x + y
        return cost

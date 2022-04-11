class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        n = len(heights)
        ladder = []

        for i in range(n - 1):
            diff = heights[i+1] - heights[i]
            if diff <= 0: continue

            heappush(ladder, diff)
            if len(ladder) > ladders:
                bricks -= heappop(ladder)
            if bricks < 0: return i

        return n - 1

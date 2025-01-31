class Solution:
    def findRadius(self, houses, heaters):
        houses, heaters, furthest = sorted(houses), sorted(heaters), 0
        for house in houses:
            idx = bisect_left(heaters, house)
            left = float('-inf') if not idx else heaters[idx - 1]
            right = float('inf') if idx == len(heaters) else heaters[idx]
            furthest = max(furthest, min(house - left, right - house))
        return furthest

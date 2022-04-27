class Solution:
    def minRefuelStops(self, target, fuel, stations):
        stops, reserves = 0, []
        for pos, gain in stations:
            while pos > fuel and reserves:
                fuel += -heappop(reserves)
                stops += 1
            if pos > fuel: return -1
            heappush(reserves, -gain)

        while target > fuel and reserves:
            fuel += -heappop(reserves)
            stops += 1

        if target > fuel: return -1
        return stops

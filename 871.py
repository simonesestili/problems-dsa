class Solution:
    def minRefuelStops(self, target, fuel, stations):
        stops, reserves = 0, []
        for pos, gas in stations:
            while pos > fuel:
                if not reserves: return -1
                fuel += -heappop(reserves)
                stops += 1
            heappush(reserves, -gas)
        while target > fuel:
            if not reserves: return -1
            fuel += -heappop(reserves)
            stops += 1
        return stops

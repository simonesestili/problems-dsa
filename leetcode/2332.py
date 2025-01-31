class Solution:
    def latestTimeCatchTheBus(self, buses, passengers, cap):
        buses, passengers, used = sorted(buses), sorted(passengers), set(passengers)

        def valid(time):
            times, j = sorted(used | {time}), 0
            for depart in buses:
                for board in range(cap):
                    if j == len(times) or times[j] > depart: break
                    j += 1
            return j > times.index(time)

        lo, hi = 1, max(buses)
        while lo < hi:
            arrival = (lo + hi + 1) // 2
            if valid(arrival): lo = arrival
            else: hi = arrival - 1
        used = set(passengers)
        while lo in used: lo -= 1
        return lo

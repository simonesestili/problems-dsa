class Solution:
    def carPooling(self, trips, cap):
        arrivals, departs = defaultdict(int), defaultdict(int)
        start, end = float('inf'), float('-inf')
        for num, src, dest in trips:
            arrivals[dest] += num
            departs[src] += num
            start, end = min(start, src), max(end, dest)

        in_car = 0
        for i in range(start, end + 1):
            in_car += departs[i] - arrivals[i]
            if in_car > cap: return False
        return True

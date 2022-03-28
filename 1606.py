from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k, arrival, load):
        requests, sl = [0] * k, SortedList(range(k))
        ends = []

        for i, (a, l) in enumerate(zip(arrival, load)):
            while ends and ends[0][0] <= a: sl.add(heappop(ends)[1])
            if len(sl) == 0: continue
            server = sl.bisect_left(i % k)
            server = sl[0] if server == len(sl) else sl[server]
            heappush(ends, (a + l, server))
            requests[server] += 1
            sl.remove(server)

        most = max(requests)
        return [i for i, r in enumerate(requests) if r == most]

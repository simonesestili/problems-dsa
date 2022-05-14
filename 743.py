class Solution:
    def networkDelayTime(self, times, n, k):
        graph, dist = defaultdict(dict), [float('inf')] * (n + 1)
        dist[0] = dist[k] = 0

        for u, v, w in times: graph[u][v] = w

        heap = [(dist[i], i) for i in range(1, n + 1)]
        heapify(heap)

        while heap:
            time, node = heappop(heap)
            for neigh, delay in graph[node].items():
                if dist[neigh] <= time + delay: continue
                heappush(heap, (time + delay, neigh))
                dist[neigh] = time + delay

        ans = max(dist)
        return -1 if ans == float('inf') else ans

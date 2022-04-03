class Solution:
    def networkDelayTime(self, times, n, k):
        graph, dist = defaultdict(list), [float('inf')] * (n + 1)
        dist[0] = dist[k] = 0

        for u, v, w in times: graph[u].append((v, w))

        heap = [(dist[i], i) for i in range(1, n + 1)]
        heapify(heap)

        while heap:
            time, node = heappop(heap)
            for to, weight in graph[node]:
                if time + weight < dist[to]:
                    heappush(heap, (time + weight, to))
                    dist[to] = time + weight

        ans = max(dist)
        return -1 if ans == float('inf') else ans

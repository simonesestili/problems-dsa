class Solution:
    def minimumWeight(self, n, edges, src1, src2, dest):
        graph1, graph2 = defaultdict(list), defaultdict(list)
        for u, v, w in edges: graph1[u].append((v, w)), graph2[v].append((u, w))

        def dijkstra(graph, src):
            heap, times = [(0, src)], defaultdict(int)
            while heap:
                time, node = heappop(heap)
                if node not in times:
                    times[node] = time
                    for u, w in graph[node]:
                        heappush(heap, (time + w, u))

            return [times.get(i, float('inf')) for i in range(n)]

        arr1 = dijkstra(graph1, src1)
        arr2 = dijkstra(graph1, src2)
        arr3 = dijkstra(graph2, dest)
            
        ans = float('inf')
        for i in range(n): ans = min(ans, arr1[i] + arr2[i] + arr3[i])
        return ans if ans != float('inf') else -1

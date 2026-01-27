class Solution:
    def minCost(self, n, edges):
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w*2))

        seen, q = defaultdict(lambda: inf, {0: 0}), [(0, 0)]
        while q:
            cost, u = heappop(q)
            if u == n - 1:
                return cost
            for v, w in graph[u]:
                if cost + w < seen[v]:
                    heappush(q, (cost + w, v))
                    seen[v] = cost + w
        return -1

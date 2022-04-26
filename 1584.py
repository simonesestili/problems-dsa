class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        graph = [[float('inf')] * n for _ in range(n)]

        for i, (xi, yi) in enumerate(points):
            for j, (xj, yj) in enumerate(points):
                if i == j: continue
                graph[i][j] = abs(xi - xj) + abs(yi - yj)

        heap = [(graph[0][j], 0, j) for j in range(1, n)]
        heapify(heap)

        cost, seen = 0, set([0])
        while len(seen) < n:
            w, u, v = heappop(heap)
            if v in seen: continue
            [heappush(heap, (graph[v][z], v, z)) for z in range(n) if z != v]
            seen.add(v)
            cost += w

        return cost


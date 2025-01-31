class Solution:
    def findTheCity(self, n, edges, mx):
        dist = [[0 if i == j else inf for i in range(n)] for j in range(n)]
        for u, v, w in edges: dist[u][v] = dist[v][u] = w
        for x in range(n):
            for u in range(n):
                for v in range(n):
                    dist[u][v] = min(dist[u][v], dist[u][x] + dist[x][v])
        counts = {sum(dist[i][j] <= mx for j in range(n)): i for i in range(n)}
        return counts[min(counts.keys())]


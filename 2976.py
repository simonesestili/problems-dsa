class Solution:
    def minimumCost(self, src, dest, original, changed, cost):
        code = lambda c: ord(c) - ord('a')
        dist = [[0 if i == j else inf for j in range(26)] for i in range(26)]
        for u, v, c in zip(original, changed, cost):
            dist[code(u)][code(v)] = min(dist[code(u)][code(v)], c)
        for x in range(26):
            for u in range(26):
                for v in range(26):
                    dist[u][v] = min(dist[u][v], dist[u][x] + dist[x][v])
        ans = sum(dist[code(u)][code(v)] for u, v in zip(src, dest))
        return -1 if ans == inf else ans


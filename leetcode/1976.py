MOD = 10 ** 9 + 7
class Solution:
    def countPaths(self, n, roads):
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        h, dists = [(0, 0)], {0: 0}
        while True:
            node, cost = heappop(h)
            if node == n - 1:
                break

            for ch, w in graph[node]:
                if ch not in dists or cost + w < dists[ch]:
                    dists[ch] = cost + w
                    heappush(h, (ch, dists[ch]))

        @cache
        def dp(node):
            if node == n - 1:
                return 1

            ans = 0
            for ch, w in graph[node]:
                if dists[node] + w == dists[ch]:
                    ans = (ans + dp(ch)) % MOD

            return ans

        return dp(0)

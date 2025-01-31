class Solution:
    def maximumDetonation(self, bombs):
        graph = self.parse(bombs)

        def dfs(bomb, gone):
            if bomb in gone: return 0
            ans = 1
            gone.add(bomb)
            for j in graph[bomb]:
                ans += dfs(j, gone.copy())
            return ans

        return max(dfs(i, set()) for i in range(len(bombs))

    def parse(self, bombs):
        graph, n = defaultdict(list), len(bombs)
        for i, (x, y, r) in enumerate(bombs):
            for j, (xx, yy, rr) in enumerate(bombs):
                if i == j: continue
                if pow(xx - x, 2) + pow(yy - y, 2) <= r * r:
                    graph[i].append(j)
        return graph

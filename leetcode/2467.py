class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q, parents, depths = deque([0]), {0: -1}, {0: 0}
        while q:
            node = q.popleft()
            for ch in graph[node]:
                if ch not in parents:
                    parents[ch] = node
                    depths[ch] = depths[node] + 1
                    q.append(ch)

        curr = bob
        while depths[curr] > depths[bob] // 2:
            amount[curr] = 0
            curr = parents[curr]
        if depths[bob] % 2 == 0:
            amount[curr] //= 2

        seen = set([0])
        def dfs(node):
            return amount[node] + max(((seen.add(ch), dfs(ch))[1] for ch in graph[node] if ch not in seen), default=0)

        return dfs(0)

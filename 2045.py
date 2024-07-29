class Solution:
    def secondMinimum(self, n, edges, time, change):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans, q, seen = None, deque([(1, 0)]), defaultdict(list)
        while q:
            u, d = q.popleft()
            if u == n:
                if ans is None: ans = d
                elif d > ans: return d
            if d // change % 2: d = (d // change + 1) * change
            d += time
            for v in graph[u]:
                if not seen[v] or len(seen[v]) == 1 and seen[v][0] != d:
                    seen[v].append(d)
                    q.append((v, d))


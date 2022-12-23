class Solution:
    def validPath(self, n, edges, src, dst):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q, seen = deque([src]), set([src])
        while q:
            node = q.popleft()
            if node == dst: return True
            for neigh in graph[node]:
                if neigh in seen: continue
                seen.add(neigh)
                q.append(neigh)

        return False

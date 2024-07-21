class Solution:
    def buildMatrix(self, k, rowconds, colconds):

        def topsort(conds):
            graph = defaultdict(list)
            indeg = defaultdict(int)
            for u, v in conds:
                graph[u].append(v)
                indeg[v] += 1
            ans, q = [], deque(u for u in range(1, k+1) if indeg[u] == 0)
            while q:
                u = q.popleft()
                ans.append(u)
                for v in graph[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0: q.append(v)
            return ans if len(ans) == k else []

        rows, cols = topsort(rowconds), topsort(colconds)
        if not rows or not cols: return []
        rows = {x: i for i, x in enumerate(rows)}
        cols = {x: i for i, x in enumerate(cols)}
        mat = [[0] * k for _ in range(k)]
        for x in range(1, k+1): mat[rows[x]][cols[x]] = x
        return mat


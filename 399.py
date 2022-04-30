class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((v, b))
            graph[b].append((1/v, a))

        def query(c, d):
            if c not in graph or d not in graph: return -1
            queue, seen = deque([(1, c)]), set([c])
            while queue:
                val, var = queue.popleft()
                if var == d: return val
                for val2, var2 in graph[var]:
                    if var2 in seen: continue
                    queue.append((val * val2, var2))
                    seen.add(var2)
            return -1

        return [query(c, d) for c, d in queries]

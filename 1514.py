class Solution:
    def maxProbability(self, n, edges, prob, start, end):
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            if prob[i] == 0: continue
            graph[u].append((v, prob[i]))
            graph[v].append((u, prob[i]))

        q, seen = [(-1, start)], set()
        while q:
            up, u = heappop(q)
            if u == end: return -up
            seen.add(u)
            for v, vp in graph[u]:
                if v in seen: continue
                heappush(q, (up * vp, v))

        return 0


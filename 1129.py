class Solution:
    def shortestAlernatingPaths(self, n, reds, blues):
        graph = defaultdict(set)
        ans = [-1] * n
        for a, b in reds: graph[a].add((b, -1))
        for u, v in blues: graph[u].add((v, 1))

        queue, seen = deque([(0, 0)]), set([(0, 0)])
        while queue:
            node, edge = queue.popleft()

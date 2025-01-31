class Solution:
    def findOrder(self, n, reqs):
        self.graph = defaultdict(list) 
        for a, b in reqs: self.graph[b].append(a)

        self.path, self.seen = [], [0] * n
        for i in range(n):
            if not self.dfs(i):
                return []

        return [] if len(self.path) < n else self.path[::-1]

    def dfs(self, node):
        if self.seen[node]:
            return self.seen[node] == 1
        self.seen[node] = -1
        for neigh in self.graph[node]:
            if not self.dfs(neigh):
                return False
        self.seen[node] = 1
        self.path.append(node)
        return True

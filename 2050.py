class Solution:
    def minimumTime(self, n, relations, time):
        self.graph, self.times = defaultdict(list), [0] * n
        for prev, nextt in relations:
            self.graph[nextt - 1].append(prev - 1)

        def dfs(idx):
            if self.times[idx]: return
            self.times[idx] = time[idx]
            extra = 0
            for prev in self.graph[idx]:
                dfs(prev)
                extra = max(extra, self.times[prev])
            self.times[idx] += extra

        for i in range(n): dfs(i)
        return max(self.times)

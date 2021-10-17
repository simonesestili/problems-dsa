class Solution:
    def secondMinimum(self, n, edges, time, change):
        dirs = defaultdict(set)
        for u, v in edges:
            dirs[u].add(v)
            dirs[v].add(u)
        minimum = [[float('inf'), float('inf')] for _ in range(n+1)]
        minimum[1][0] = 0
        curr = deque([1])
        seen = set()
        while curr:
            node = curr.pop()
            if node in seen:
                continue
            for to in dirs[node]:
                if minimum[to][0] == float('inf'):
                    prev = minimum[node][0]
                    isGreen = self.isGreen(prev, change)
                    diff = time + (prev if isGreen else (prev // change + 1) * change)
                    minimum[to][0] = min(minimum[to][0], diff)
                    curr.appendleft(to)
                elif minimum[to][1] == float('inf'):
                    prev = minimum[node][1]
                    isGreen = self.isGreen(prev, change)
                    diff = time + (prev if isGreen else (prev // change + 1) * change)
                    minimum[to][1] = min(minimum[to][1], diff)
                    curr.appendleft(to)
                else:
                    seen.add(to)
        return minimum[n][1]

    def isGreen(self, time, change):
        return not (time // change % 2)

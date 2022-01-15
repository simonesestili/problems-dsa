class Solution:
    def minJumps(self, arr):
        n, groups = len(arr), defaultdict(list)
        for i, x in enumerate(arr): groups[x].append(i)
        costs = [float('inf')] * n

        def bfs(i, prev):
            if prev + 1 >= costs[i]: return
            costs[i] = prev + 1
            for j in groups[arr[i]]: bfs(j, costs[i])
            if i: bfs(i - 1, costs[i])
            if i != n - 1: bfs(i + 1, costs[i])

        bfs(0, -1)
        return costs[-1]

class Solution:
    def gardenNoAdj(self, n, paths):
        types = [0] * n
        graph = defaultdict(list)
        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)
        
        for i in range(n):
            types[i] = (set([1, 2, 3, 4]) - set([types[j] for j in graph[i]])).pop()

        return types

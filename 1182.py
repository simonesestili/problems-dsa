class Solution:
    def shortestDistanceColor(self, colors, queries):
        n = len(colors)
        dists = [[float('inf')] * 3 for _ in range(n)]

        prev = [float('inf')] * 3
        for i in range(n - 1, -1, -1):
            prev[colors[i] - 1] = i
            dists[i] = [x - i for x in prev]

        prev = [float('-inf')] * 3
        for i in range(n):
            prev[colors[i] - 1] = i
            dists[i] = [min(dists[i][c], i - x) for c, x in enumerate(prev)]

        conv = lambda x: -1 if x == float('inf') else x
        return [conv(dists[i][c-1]) for i, c in queries]

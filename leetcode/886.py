class Solution:
    def possibleBipartition(self, n, dislikes):
        graph = [list() for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        colors = [0] * (n + 1)
        def color(node, col):
            if colors[node]: return colors[node] == col
            colors[node] = col
            for neigh in graph[node]:
                if not color(neigh, -col):
                    return False
            return True

        return all(color(i, colors[i] or 1) for i in range(1, n + 1))

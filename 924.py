class Solution:
    def minMalwareSpread(self, graph, initial):
        n = len(graph)
        initial.sort()
        parents = [i for i in range(n)]

        def parent(node):
            while parents[node] != node:
                node = parents[node]
            return node    

        ranks = [1] * n 
        for u in range(n):
            for v in range(n):
                # If we have an edge and the nodes are not in the same SCC: union them
                up, vp = parent(u), parent(v)
                if u != v and graph[u][v] and up != vp:
                    if ranks[up] > ranks[vp]:
                        parents[vp] = up
                        ranks[up] += ranks[vp]
                    else:
                        parents[up] = vp
                        ranks[vp] += ranks[up]
        malware = [0] * n
        for node in initial:
            malware[parent(node)] += 1
        ans = initial[0]
        group = 0
        for node in initial:
            p = parent(node)
            if malware[p] == 1 and ranks[p] > group:
                group = ranks[p]
                ans = node
        return ans

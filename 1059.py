class Solution:
    def leadsToDestination(self, n, edges, src, dest):
        graph = defaultdict(list)
        for a, b in edges: graph[a].append(b)
        
        def dfs(node, seen=set()):
            if node in seen: return False
            if not graph[node]: return node == dest
            seen.add(node)
            ans = not any(not dfs(j, seen) for j in graph[node])
            seen.remove(node)
            return ans

        return dfs(src)

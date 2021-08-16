class Solution:
    def allPathsSourceTarget(self, graph):
        paths = []
        self.path(graph, paths, [])
        return paths
        
    def path(self, graph, paths, curr_path, curr=0):
        curr_path.append(curr)
        if curr == len(graph) - 1:
            paths.append(curr_path[:])
            return
        
        for node in graph[curr]:
            self.path(graph, paths, curr_path[:], node)

print(Solution().allPathsSourceTarget(
[[4,3,1],[3,2,4],[3],[4],[]]))
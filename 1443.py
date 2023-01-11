class Solution:
    def minTime(self, n, edges, apples):
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        self.ans = 0
        def dfs(node, parent=None):
            v = apples[node]
            for child in tree[node]:
                if child != parent and dfs(child, node):
                    self.ans += 1
                    v = True
            return v

        dfs(0)
        return self.ans * 2

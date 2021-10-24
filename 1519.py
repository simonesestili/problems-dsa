class Solution:
    def countSubTrees(self, n, e, labels):
        self.ans = [0] * n
        edges = defaultdict(list)
        for a, b in e:
            edges[a].append(b)
            edges[b].append(a)
            
        def dfs(curr, parent):
            c = Counter()
            for child in edges[curr]:
                if child != parent:
                    c += dfs(child, curr)
            c[labels[curr]] += 1
            self.ans[curr] = c[labels[curr]]
            return c

        dfs(0, -1)
        return self.ans

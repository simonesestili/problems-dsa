class Solution:
    def countSubTrees(self, n, edges, labels):
        ans, tree = [0] * n, defaultdict(list)
        for a, b in edges: tree[a].append(b); tree[b].append(a)

        def dfs(node, parent=None):
            counts = defaultdict(int)
            counts[labels[node]] = 1
            for child in tree[node]:
                if child == parent: continue
                for label, count in dfs(child, node).items():
                    counts[label] += count
            ans[node] = counts[labels[node]]
            return counts

        dfs(0)
        return ans

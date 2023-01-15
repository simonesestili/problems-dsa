class Solution:
    def longestPath(self, parents, s):
        n, tree = len(parents), defaultdict(list)
        for child, parent in enumerate(parents[1:]): tree[parent].append(child+1)

        @cache
        def dfs(node):
            return 1 + max((dfs(child) for child in tree[node] if s[node] != s[child]), default=0)

        [dfs(node) for node in range(n)]
        return max(1 + sum(nlargest(2, (dfs(child) for child in tree[node] if s[node] != s[child]))) for node in range(n))

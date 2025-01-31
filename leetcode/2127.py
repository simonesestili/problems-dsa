class Solution:
    def maximumInvitations(self, favorite):
        n = len(favorite)
        self.ans = 0

        # Find the largest cycle
        seen, cycle = set(), {}
        def dfs(node, idx):
            if node in seen:
                self.ans = max(self.ans, idx - cycle.get(node, inf))
                return

            seen.add(node)
            cycle[node] = idx
            dfs(favorite[node], idx + 1)

        for node in range(n):
            dfs(node, 0)
            cycle.clear()

        # Find largest branches for all coupled nodes
        inv = defaultdict(list)
        for u, v in enumerate(favorite):
            inv[v].append(u)

        sources = set()
        def dfs(node):
            return 1 + max((dfs(to) for to in inv[node] if to not in sources), default=0)

        ans2 = 0
        for node in range(n):
            if favorite[favorite[node]] != node or favorite[node] in sources:
                continue
            sources.add(node)
            sources.add(favorite[node])
            ans2 += dfs(node) + dfs(favorite[node])

        return max(self.ans, ans2)

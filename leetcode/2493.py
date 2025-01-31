class Solution:
    def magnificentSets(self, n, edges):
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

        def dfs(node, group):
            if node in group:
                return
            group.add(node)
            for ch in self.graph[node]:
                dfs(ch, group)

        ans, seen = 0, set()
        for node in range(1, n + 1):
            if node not in seen:
                group = set()
                dfs(node, group)
                subans = self.solve(group)
                if subans == -1:
                    return -1
                ans += subans
                seen |= group

        return ans

    def solve(self, group):
        ans = 0
        for root in group:
            q, depths = deque([(root, 0)]), {root: 0}
            while q:
                node, depth = q.popleft()
                ans = max(ans, depth + 1)
                for ch in self.graph[node]:
                    if ch not in depths:
                        q.append((ch, depth + 1))
                        depths[ch] = depth + 1
                    elif abs(depths[ch] - depth) != 1:
                        return -1

        return ans

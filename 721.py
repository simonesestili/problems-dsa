class Solution:
    def accountsMerge(self, accounts):
        n, links = len(accounts), defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                links[email].append(i)

        dsu = DSU(n)
        for email in links:
            owners = links[email]
            for i in range(len(owners) - 1):
                dsu.union(owners[i], owners[i + 1])

        merged = defaultdict(set)
        for email in links:
            group = dsu.find(links[email][0])
            merged[group].add(email)
        return [[accounts[group][0]] + sorted(merged[group]) for group in merged]

class DSU:
    def __init__(self, n):
        self.reps = list(range(n))
        self.ranks = [1] * n

    def find(self, node):
        while node != self.reps[node]:
            node = self.reps[node]
        return node

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if self.ranks[ap] < self.ranks[bp]:
            ap, bp = bp, ap
        if ap != bp:
            self.reps[bp] = ap
            self.ranks[ap] += self.ranks[bp]


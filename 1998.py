class Solution:
    def gcdSort(self, nums):
        dsu, groups = DSU(len(nums)), defaultdict(list)
        indices = defaultdict(list)
        for i, x in enumerate(nums):
            indices[x].append(i)
            for p in self.primes(x):
                groups[p].append(i)

        for p in groups:
            for i in range(len(groups[p]) - 1):
                dsu.union(groups[p][i], groups[p][i + 1])

        for i, x in enumerate(sorted(nums)):
            if dsu.find(i) != dsu.find(indices[x].pop()):
                return False

        return True


    def primes(self, x):
        primes = set()
        for i in range(2, int(sqrt(x)) + 1):
            while not x % i:
                primes.add(i)
                x //= i
        if x != 1: primes.add(x)
        return primes

class DSU:
    def __init__(self, n):
        self.reps = list(range(n))
        self.ranks = [1] * n

    def find(self, a):
        while a != self.reps[a]:
            a = self.reps[a]
        return a

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap != bp:
            if self.ranks[ap] > self.ranks[bp]:
                self.reps[bp] = ap
                self.ranks[ap] += self.ranks[bp]
            else:
                self.reps[ap] = bp
                self.ranks[bp] += self.ranks[ap]
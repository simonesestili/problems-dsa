class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n

    def find(self, node):
        while node != self.parents[node]:
            node = self.parents[node]
        return node

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap != bp:
            if self.ranks[ap] > self.ranks[bp]:
                self.parents[bp] = ap
                self.ranks[ap] += self.ranks[bp]
            else:
                self.parents[ap] = bp
                self.ranks[bp] += self.ranks[ap]

class Solution:
    def largestComponentSize(self, nums):
        indices = {val: i for i, val in enumerate(nums)}
        primes = defaultdict(list)
        for num in nums:
            for prime in self.get_primes(num):
                primes[prime].append(num)
        uf = DSU(len(nums))
        for nums in primes.values():
            for i in range(len(nums) - 1):
                uf.union(indices[nums[i]], indices[nums[i + 1]])
        return max(uf.ranks)

    def get_primes(self, x):
        primes = set()
        while not x % 2:
            primes.add(2)
            x //= 2
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            while not x % i:
                primes.add(i)
                x //= i
        if x > 1:
            primes.add(x)
        return list(primes)

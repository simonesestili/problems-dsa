class Solution:
    def numberOfPairs(self, a, b, k):
        factors = defaultdict(int)
        for x in a:
            for i in range(1, int(sqrt(x)) + 1):
                if x % i: continue
                factors[i] += 1
                if i*i != x: factors[x//i] += 1

        return sum(factors[x*k] for x in b)


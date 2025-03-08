class Solution
    def closestPrimes(self, left, right):
        prime = [False, False] + [True] * right

        for p in range(2, int(sqrt(right)) + 1):
            if not prime[p]: continue
            for x in range(p * p, right + 1, p):
                prime[x] = False

        primes = [x for x, p in enumerate(prime) if left <= x <= right and p]
        return min([[primes[i], primes[i+1]] for i in range(len(primes)-1)], key=lambda x: x[1] - x[0], default=[-1, -1])

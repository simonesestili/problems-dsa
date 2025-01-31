class Solution:
    def countPrimes(self, n):
        if n < 2: return 0
        sieve = [True] * n
        sieve[0] = sieve[1] = False
        for i in range(2, n):
            if not sieve[i]: continue
            for j in range(i * i, n, i):
                sieve[j] = False
        return len([x for x in sieve if x])


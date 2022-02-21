class Solution:
    def numPrimeArrangements(self, n):
        MOD = pow(10, 9) + 7
        
        def isprime(x):
            for i in range(2, int(sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True

        def fact(x):
            res = 1
            for i in range(2, x + 1):
                res = res * i % MOD
            return res

        primes = sum(isprime(i) for i in range(2, n + 1))
        return fact(primes) * fact(n - primes) % MOD

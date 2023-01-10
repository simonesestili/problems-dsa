class Solution:
    def distinctPrimeFactors(self, nums):
        primes = set()
        for x in nums:
            for i in range(2, int(sqrt(x)) + 1):
                while x % i == 0:
                    primes.add(i)
                    x //= i
            if x != 1: primes.add(x)
        return len(primes)

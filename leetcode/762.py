PRIMES = {2, 3, 5, 7, 11, 13, 17, 19}
class Solution:
    def countPrimeSetBits(self, left, right):
        return sum(x.bit_count() in PRIMES for x in range(left, right + 1))

class Solution:
    def isThree(self, n):
        return n != 1 and int(sqrt(n)) == sqrt(n) and self.is_prime(sqrt(n))

    def is_prime(self, n):
        for i in range(2, int(sqrt(n)) + 1):
            if not n % i: return False
        return True

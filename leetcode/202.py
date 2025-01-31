class Solution:
    def isHappy(self, n):
        seen = set()
        while n != 1:
            if n in seen: return False
            seen.add(n)
            n = self.digital(n)
        return True

    def digital(self, n):
        total = 0
        while n:
            total += pow(n % 10, 2)
            n //= 10
        return total

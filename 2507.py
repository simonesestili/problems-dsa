class Solution:
    def smallestValue(self, n):
        while True:
            prev, new = n, 0
            for i in range(2, n + 1):
                while n % i == 0:
                    new += i
                    n //= i
            n = new
            if prev == new: break
        return n

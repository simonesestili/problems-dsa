class Solution:
    def myPow(self, x, n):
        if n <= 0:
            return 1 if not n else 1 / self.myPow(x, -n)
        if n & 1:
            return x * self.myPow(x * x, n // 2)
        return self.myPow(x * x, n // 2)

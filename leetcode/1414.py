class Solution:
    def findMinFibonacciNumbers(self, k):
        if not k: return 0
        a = b = 1
        while b <= k:
            a, b = b, a + b
        return 1 + self.findMinFibonacciNumbers(k - a)


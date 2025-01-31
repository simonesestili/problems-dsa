class Solution:
    def lastRemaining(self, n, left=True):
        if n <= 2: 
            return 1 if n == 1 or not left else 2
        if left:
            return 2 * self.lastRemaining(n // 2, False)
        elif n % 2:
            return 2 * self.lastRemaining(n // 2, True)
        else:
            return 2 * self.lastRemaining(n // 2, True) - 1

class Solution:
    def differenceOfSums(self, n, m):
        total = (n * n + n) // 2
        rem = n // m
        rem = m * (rem * rem + rem) // 2
        return total - rem - rem

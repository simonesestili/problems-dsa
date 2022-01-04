class Solution:
    def isArmstrong(self, n):
        total, m, x = 0, len(str(n)), n
        while x:
            total += pow(x % 10, m)
            x //= 10
        return total == n
